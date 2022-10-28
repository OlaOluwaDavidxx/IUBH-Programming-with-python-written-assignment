import pandas as pd
from middleware.evaluate_score import squared_error
from .CONSTANTS import match_label, trained_list


def find_ideal(ideal, train, y_label):
    """
    Function to find the ideal dataset
    :param ideal: ideal dataset
    :param train: train dataset
    :param y_label: y label
    :return: the squared deviations
    """
    squared_deviations = pd.DataFrame()

    for column in ideal.columns:
        squared_deviations[column] = squared_error(train[y_label], ideal[column])

    return squared_deviations.sum(axis=0).idxmin()


def find_all_ideal(ideal, train):
    """
    Function to find all ideal dataset
    :param ideal: ideal dataset
    :param train: train dataset
    :return: ideals
    """
    ideals_y = {}
    ideal = ideal.drop('x', axis=1)
    for y_label in trained_list:
        ideals_y[y_label] = find_ideal(ideal, train, y_label)

    return ideals_y


def get_points(mapping):
    """
    Get points from mapped dataset
    :param mapping: y data mapped from list of functions
    :return: x_points, y_points
    """
    try:
        x_points = mapping[mapping[match_label] == True]['x']
        y_points = mapping[mapping[match_label] == True]['y']

        return x_points, y_points

    except Exception as err:
        print(f"status: error \nerror Code: {err} \nmessage: Error has occurred while getting x and y points")
