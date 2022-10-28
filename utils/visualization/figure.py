import os
from bokeh.plotting import output_file


def save_figure(y_label, path="reports/figure/"):
    """
    Function to save figure in png format
    :param y_label: y label
    :param path: file directory
    """
    if not os.path.exists(path):
        os.makedirs(path)
    output_file(f"{path}{y_label}.html")