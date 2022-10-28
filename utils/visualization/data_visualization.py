from .plot import scatter_plot, scatter_plot_ideal, scatter_plot_with_points
from utils.utils import get_points


def visualize(data):
    """
    :param data: dataframe
    :return: scatter plot
    """
    for column in data.columns.difference(['x']):
        scatter_plot(data['x'], data[column], column)


def visualize_ideal(list_of_func):
    """
    :param list_of_func:
    :return: scatter plot for list of functions
    """
    for y in list_of_func:
        scatter_plot_ideal(y.x, y.y_train, y.y_ideal, y.y_label, y.ideal_label)


def visualize_with_points(list_of_func):
    """
    :param list_of_func:
    :return: scatter plot for list of functions
    """
    for y in list_of_func:

        x_pt, y_pt = get_points(y.mapping)
        scatter_plot_with_points(y.x, y.y_ideal, x_pt, y_pt, y.y_label)
