from bokeh.plotting import figure, show
from .figure import save_figure
from utils.CONSTANTS import width, height, tools


def scatter_plot(x, y, y_label):
    """
    Function to create scatter plot between x and y
    :param x: Given x variables
    :param y: Given y variables
    :param y_label:
    :return: create scatter plot
    """
    fig = figure(plot_width=width, plot_height=height, tools=tools)
    fig.scatter(x, y, legend_label= y_label,color="blue")
    fig.legend.location = "bottom_right"
    fig.xaxis.axis_label = 'x'
    fig.yaxis.axis_label = y_label
    fig.title = f"Initial {y_label}"
    fig.title.align = "center"
    save_figure(f"Initial {y_label}")
    show(fig)


def scatter_plot_with_points(x, y, x_pt, y_pt, y_label):
    """
    Function to create scatter plot between x and y with points
    :param x: Given x variables
    :param y: Given y variables
    :param x_pt: x coordinate of mapped points
    :param y_pt: y coordinate of mapped points
    :param y_label: y label
    :return: create scatter plot with mapped points
    """
    fig = figure(plot_width=width, plot_height=height, tools=tools)
    fig.scatter(x, y, legend_label=y_label, marker='circle')
    fig.scatter(x_pt, y_pt, legend_label="Points", marker='circle', color='red')
    fig.legend.location = "bottom_right"
    fig.title = f"Number of points: {len(x_pt)}"
    fig.title.align = "center"
    fig.xaxis.axis_label = 'x'
    fig.yaxis.axis_label = f"Ideal function for {y_label}"
    save_figure(f"With test {y_label}")
    show(fig)


def scatter_plot_ideal(x, y, y_ideal, y_label, y_ideal_label):
    """
    Function to create scatter plot between x, y, and y_ideal
    :param x: Given x variables
    :param y: Given y variables
    :param y_ideal: Given y ideal variables
    :param y_label: y label
    :param y_ideal_label: y ideal label
    :return: create scatter plot for ideal
    """
    fig = figure(plot_width=width, plot_height=height, tools=tools)
    fig.line(x, y, color='blue',legend_label=y_label, line_width=1.5)
    fig.line(x, y_ideal, legend_label=y_ideal_label, color='red', line_width=2)
    fig.legend.location = "bottom_right"
    fig.xaxis.axis_label = 'x'
    fig.yaxis.axis_label = y_label
    fig.title = f"Ideal for {y_label} is {y_ideal_label}"
    fig.title.align = "center"
    save_figure(f"Ideal for {y_label} is {y_ideal_label}")
    show(fig)
