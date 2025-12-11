import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

def draw_boxplot(x, data, log_scale=False):
    """
    Draws a boxplot for the given data.

    Parameters:
    x (str): The column name to plot.
    data (DataFrame): The DataFrame containing the data.
    log_scale (bool): Whether to use a logarithmic scale for the y-axis.
    """
    plt.figure(figsize=(10, 6))
    sns.boxplot(x=x, data=data)
    if log_scale:
        plt.yscale('log')
    plt.title(f'Boxplot of {x}')
    plt.show()

def draw_histplot(data, title, bins=50, log_scale=False):
    """
    Draws a histogram for the given data.

    Parameters:
    data (Series): The data to plot.
    title (str): The title of the plot.
    bins (int): The number of bins for the histogram.
    log_scale (bool): Whether to use a logarithmic scale for the y-axis.
    """
    plt.figure(figsize=(10, 6))
    sns.histplot(data, bins=bins)
    if log_scale:
        plt.yscale('log')
    plt.title(title)
    plt.show()

def draw_barplot(x, y, x_label, y_label, title, palette="viridis"):
    """
    Draws a bar plot for the given data.

    Parameters:
    x (list): The x-axis values.
    y (list): The y-axis values.
    x_label (str): The label for the x-axis.
    y_label (str): The label for the y-axis.
    title (str): The title of the plot.
    palette (str): The color palette to use for the plot.
    """
    plt.figure(figsize=(10, 6))
    sns.barplot(x=x, y=y, palette=palette)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.title(title)
    plt.show()

def draw_gates_plot(data, x, hue):
    """
    Draws a plot comparing different versions of the game.

    Parameters:
    data (DataFrame): The DataFrame containing the data.
    x (str): The column name to plot on the x-axis.
    hue (str): The column name to use for color encoding.
    """
    plt.figure(figsize=(10, 6))
    sns.histplot(data=data, x=x, hue=hue, multiple="stack")
    plt.title(f'Comparison of {hue} versions')
    plt.show()

def plot_mean_game_rounds_with_ci(versions, mean_values, ci_lowers, ci_uppers, ci):
    """
    Plots the mean game rounds with confidence intervals.

    Parameters:
    versions (list): The list of versions.
    mean_values (list): The list of mean values for each version.
    ci_lowers (list): The list of lower bounds of the confidence intervals.
    ci_uppers (list): The list of upper bounds of the confidence intervals.
    ci (int): The confidence interval percentage.
    """
    plt.figure(figsize=(8, 4))
    yerr_lower = [mean - ci_lower for mean, ci_lower in zip(mean_values, ci_lowers)]
    yerr_upper = [ci_upper - mean for mean, ci_upper in zip(mean_values, ci_uppers)]
    plt.errorbar(versions, mean_values, yerr=[yerr_lower, yerr_upper], fmt='o', capsize=5)
    plt.title(f'Mean Game Rounds with {ci}% Confidence Intervals')
    plt.xlabel('Version')
    plt.ylabel('Mean Game Rounds')
    plt.show()
