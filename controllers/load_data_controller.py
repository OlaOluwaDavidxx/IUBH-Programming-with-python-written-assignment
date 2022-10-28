import pandas as pd
from middleware.errorhandlers import EmptyColumnX, EmptyColumnY, DataTypeError, FileError


def check_data_columns(data):
    """
    Check dataset if it contains x and y features
    :param data: dataset (train, test or ideal datasets)
    :return: raises an error if any of the features is found missing
    """
    if "x" not in data.columns:
        raise EmptyColumnX(data)
    if len(data.columns) < 2:
        raise EmptyColumnY(data)


def check_data_type(data):
    """
    Check that all dataset type is numerical
    :param data: dataset (train, test or ideal datasets)
    :return: raises an error if dataset type is not numerical
    """
    if data.shape != data._get_numeric_data().shape:
        raise DataTypeError()


def load_data(filename):
    """
    Check and load csv files
    :param filename: file name
    :return: dataframe from csv
    """
    try:
        data = pd.read_csv(filename)
        check_data_columns(data)
        check_data_type(data)
        return data
    except FileNotFoundError:
        raise FileError()
