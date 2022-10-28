import pandas as pd

from configure_working_env import config
from controllers.data_perpresentation import init_data, init_ideal
from controllers.final_data_format import final_data
from controllers.load_data_controller import load_data
from database.to_db import push_to_db
from model.modelling import check_test_with_ideal
from utils.visualization.data_visualization import visualize_ideal, visualize_with_points, visualize
from utils.utils import find_all_ideal


def main():
    """
    The main script that runs the software
    """
    # check working environment
    config()

    # Load the test, train and ideal datasets
    test, train, ideal = load_data('dataset/test.csv'), load_data('dataset/train.csv'), load_data('dataset/ideal.csv')

    # Migrate dataset to the database
    push_to_db(train, "training")
    push_to_db(ideal, "ideal")

    # Change the names of the columns
    train.columns = [f"{column}_train" if column != 'x' else 'x' for column in train.columns]

    # Initialize the dataset as Data object
    list_of_func = init_data(train)

    # Find all ideal functions
    all_ideals_y = find_all_ideal(ideal, train)

    # Initialize the list of functions
    list_of_func = init_ideal(ideal, list_of_func, all_ideals_y)

    # Visualize ideal dataset
    visualize_ideal(list_of_func)

    # Test for ideal
    for y in list_of_func:
        y.mapping = check_test_with_ideal(test, train, ideal, y.y_label, y.ideal_label)

    # Visualize training datasets
    visualize(train)
    # Visualize test datasets
    visualize(test)

    # the ideal points on train dataset visualization
    visualize_with_points(list_of_func)

    y1, y2, y3, y4 = list_of_func

    delta = pd.DataFrame([y1.mapping.delta, y2.mapping.delta, y3.mapping.delta, y4.mapping.delta]).max()
    match = pd.DataFrame([y2.mapping.matched, y1.mapping.matched, y3.mapping.matched, y4.mapping.matched]).sum()

    # Migrate the final dataframe to the database
    final_dataframe = final_data(test, delta, match)
    push_to_db(final_dataframe, "Final Data")
    final_dataframe.to_csv("ideal_test_data_mapping.csv")

    print("\nProgram has run successfully...")


if __name__ == "__main__":
    main()
