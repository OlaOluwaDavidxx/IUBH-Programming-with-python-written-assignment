from utils.CONSTANTS import trained_list
from .data import Data


def init_data(train, trained_list=trained_list):
    """
    Initialize the train dataset
    :param train: the train dataset
    :param trained_list: the train dataset label
    :return: y1, y2, y3, and y4
    """
    y1, y2, y3, y4 = Data(train['x'], y_label=trained_list[0]), Data(train['x'], y_label=trained_list[1]),\
                     Data(train['x'], y_label=trained_list[2]), Data(train['x'], y_label=trained_list[3])

    list_of_func = (y1, y2, y3, y4)

    for y in list_of_func:
        y.sign_y_train(train)

    return y1, y2, y3, y4


def init_ideal(ideal, list_of_func, ideal_y):
    """
    Initialize the ideal datasets
    :param ideal: ideal datasets
    :param list_of_func:
    :param ideal_y:
    :return:
    """
    for y in list_of_func:
        y.ideal_label = ideal_y[y.y_label]
        y.sign_y_ideal(ideal)

    return list_of_func
