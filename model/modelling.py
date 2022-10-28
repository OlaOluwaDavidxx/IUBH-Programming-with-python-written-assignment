import functools as ft

import numpy as np
import pandas as pd

from utils.CONSTANTS import delta_label, match_label


def check_test_with_ideal(test, train, ideal, y_label, ideal_label):
    """
    Test the ideal dataset
    :param test:
    :param train:
    :param ideal:
    :param y_label:
    :param ideal_label:
    :return:
    """
    try:
        dfs = [test, train, ideal[['x', ideal_label]]]
        data = ft.reduce(lambda left, right: pd.merge(left, right, on='x'), dfs)

        data[delta_label] = np.abs(data[ideal_label] - data['y']) - \
                            np.sqrt(2) * np.abs(data[y_label] - data[ideal_label])
        data[match_label] = data[delta_label] <= 0

        mapping = data[['x', 'y', ideal_label, delta_label, match_label]]
        return mapping

    except Exception as err:
        print(f"status: error \nerror Code: {err} \nmessage: Error has occurred while testing the datasets.")
