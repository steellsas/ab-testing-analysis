from typing import Optional
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

FIGURE_SIZE = (8, 6)

def get_outliers_mask_iqr(ds: pd.Series) -> pd.Series:
    """
    Detects outliers in pandas series using the IQR method.

    Args:
        ds (pd.Series): Input data series containing the data.

    Returns:
        pd.Series: Boolean series indicating the presence of outliers.
    """
    q1 = ds.quantile(0.25)
    q3 = ds.quantile(0.75)
    iqr = q3 - q1

    lower_bound = q1 - 1.5 * iqr
    upper_bound = q3 + 1.5 * iqr

    return (ds < lower_bound) | (ds > upper_bound)

def draw_histplot(
    data: pd.Series,
    title: Optional[str] = None,
    x_label: Optional[str] = None,
    y_label: str = "Frequency",
    bins: int = 20,
    show_kde: bool = True,
    fig_size: tuple[int, int] = FIGURE_SIZE,
    log_scale: bool = False,
    *args,
    **kwargs,
) -> None:
    """
    Creates a histogram plot showing the distribution.

    Args:
        data (pd.Series): Data to be plotted.
        title (Optional[str]): Title of the plot.
        x_label (Optional[str]): Label for x-axis.
        y_label (str): Label for y-axis. Defaults to 'Frequency'.
        bins (int): Number of bins for the histogram. Defaults to 20.
        show_kde (bool): Whether to show the KDE line. Defaults to True.
        fig_size (tuple[int, int]): Tuple of (width, height) for the figure. Defaults to (8, 6).
        log_scale (bool): Whether to use log scale. Defaults to False.
    """
    plt.figure(figsize=fig_size)
    sns.histplot(data, bins=bins, kde=show_kde, log_scale=log_scale, **kwargs)
    plt.title(title)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.show()

def draw_barplot(
    x: pd.Series,
    y: pd.Series,
    title: Optional[str] = None,
    x_label: Optional[str] = None,
    y_label: Optional[str] = None,
    fig_size: tuple[int, int] = FIGURE_SIZE,
    **kwargs,
) -> None:
    """
    Create a bar plot.

    Args:
        x (pd.Series): X axis data.
        y (pd.Series): Y axis data.
        title (Optional[str]): Plot title. Defaults to None.
        x_label (Optional[str]): Label for x-axis. Defaults to None.
        y_label (Optional[str]): Label for y-axis. Defaults to None.
        fig_size (tuple[int, int]): Figure size. Defaults to FIGURE_SIZE.
    """
    plt.figure(figsize=fig_size)
    ax = sns.barplot(y=y, x=x, **kwargs)
    plt.title(title)
    plt.xlabel(x_label)
    plt.ylabel(y_label)

    for p in ax.patches:
        if p.get_height() > 0:
            ax.annotate(
                f"{round(p.get_height(), 1)}",
                (p.get_x() + p.get_width() / 2.0, p.get_height()),
                ha="center",
                va="center",
                fontsize=10,
                color="black",
                xytext=(0, 5),
                textcoords="offset points",
            )
    plt.show()

def draw_countplot(
    data: pd.Series,
    *args,
    title: Optional[str] = None,
    x_label: Optional[str] = None,
    y_label: Optional[str] = None,
    fig_size: tuple[int, int] = FIGURE_SIZE,
    **kwargs,
) -> None:
    """
    Create a count plot.

    Args:
        data (pd.Series): Data to be plotted.
        title (Optional[str]): Plot title. Defaults to None.
        x_label (Optional[str]): Label for x-axis. Defaults to None.
        y_label (Optional[str]): Label for y-axis. Defaults to None.
        fig_size (tuple[int, int]): Figure size. Defaults to FIGURE_SIZE.
    """
    plt.figure(figsize=fig_size)
    ax = sns.countplot(data=data, *args, **kwargs)
    plt.title(title)
    plt.xlabel(x_label)
    plt.ylabel(y_label)

    for p in ax.patches:
        ax.annotate(
            f"{p.get_height()}",
            (p.get_x() + p.get_width() / 2.0, p.get_height()),
            ha="center",
            va="center",
            fontsize=10,
            color="black",
            xytext=(0, 5),
            textcoords="offset points",
        )
    plt.show()

def draw_boxplot(
    *args,
    title: Optional[str] = None,
    x_label: Optional[str] = None,
    y_label: Optional[str] = None,
    fig_size: tuple[int, int] = FIGURE_SIZE,
    **kwargs,
) -> None:
    """
    Create a box plot.

    Args:
        title (Optional[str]): Plot title. Defaults to None.
        x_label (Optional[str]): Label for x-axis. Defaults to None.
        y_label (Optional[str]): Label for y-axis. Defaults to None.
        fig_size (tuple[int, int]): Figure size. Defaults to FIGURE_SIZE.
    """
    plt.figure(figsize=fig_size)
    sns.boxplot(*args, **kwargs)
    plt.title(title)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.show()

def plot_promotion_distributions(data: pd.DataFrame) -> None:
    """
    Plot the distribution of sales for different promotions.

    Args:
        data (pd.DataFrame): DataFrame containing sales data and promotion information.
    """
    fig, axes = plt.subplots(1, 3, figsize=(9, 3))
    sns.histplot(
        x="SalesInThousands",
        data=data[data["Promotion"] == 1],
        kde=True,
        ax=axes[0],
        label="Promotion 1",
    )
    sns.histplot(
        x="SalesInThousands",
        data=data[data["Promotion"] == 2],
        kde=True,
        ax=axes[1],
        label="Promotion 2",
    )
    sns.histplot(
        x="SalesInThousands",
        data=data[data["Promotion"] == 3],
        kde=True,
        ax=axes[2],
        label="Promotion 3",
    )

    axes[0].set_title("Promotion 1")
    axes[1].set_title("Promotion 2")
    axes[2].set_title("Promotion 3")

    common_xlim = (data["SalesInThousands"].min(), data["SalesInThousands"].max())
    common_ylim = (
        0,
        max(axes[0].get_ylim()[1], axes[1].get_ylim()[1], axes[2].get_ylim()[1]),
    )

    for ax in axes:
        ax.set_xlim(common_xlim)
        ax.set_ylim(common_ylim)

    axes[1].set_ylabel("")
    axes[2].set_ylabel("")

    plt.tight_layout()
    plt.show()

def plot_sales_distribution(data: pd.DataFrame) -> None:
    """
    Plot the distribution of sales using a histogram and a box plot.

    Args:
        data (pd.DataFrame): DataFrame containing sales data.
    """
    sns.set(style="whitegrid")

    # Create a figure with two subplots
    fig, axs = plt.subplots(1, 2, figsize=(10, 6))

    # Histogram
    sns.histplot(data["SalesInThousands"], bins=10, kde=True, ax=axs[0])
    axs[0].set_title("Distribution of Sales In Thousands (Histogram)")
    axs[0].set_xlabel("Sales In Thousands")
    axs[0].set_ylabel("Frequency")

    # Box plot
    sns.boxplot(x=data["SalesInThousands"], ax=axs[1])
    axs[1].set_title("Distribution of Sales In Thousands (Box Plot)")
    axs[1].set_xlabel("Sales In Thousands")

    # Show the plots
    plt.tight_layout()
    plt.show()

def draw_gates_plot(df: pd.DataFrame, column: str, group_col: str) -> None:
    """
    Plot histograms and box plots for different gates.

    Args:
        df (pd.DataFrame): DataFrame containing the data.
        column (str): Column name for the data to be plotted.
        group_col (str): Column name for the group labels.
    """
    fig, axes = plt.subplots(2, 2, figsize=(12, 6))

    # Histogram for gate_30
    sns.histplot(
        data=df[df[group_col] == "gate_30"], x=column, bins=50, kde=True, ax=axes[0, 0]
    )
    axes[0, 0].set_title("Histogram of {} for gate_30".format(column))
    axes[0, 0].set_xlabel(column)
    axes[0, 0].set_ylabel("Frequency")

    # Histogram for gate_40
    sns.histplot(
        data=df[df[group_col] == "gate_40"], x=column, bins=50, kde=True, ax=axes[0, 1]
    )
    axes[0, 1].set_title("Histogram of {} for gate_40".format(column))
    axes[0, 1].set_xlabel(column)
    axes[0, 1].set_ylabel("Frequency")

    # Box plot for gate_30
    sns.boxplot(data=df[df[group_col] == "gate_30"], x=column, ax=axes[1, 0])
    axes[1, 0].set_title("Box Plot of {} for gate_30".format(column))
    axes[1, 0].set_xlabel(column)

    # Box plot for gate_40
    sns.boxplot(data=df[df[group_col] == "gate_40"], x=column, ax=axes[1, 1])
    axes[1, 1].set_title("Box Plot of {} for gate_40".format(column))
    axes[1, 1].set_xlabel(column)

    plt.tight_layout()
    plt.show()

def plot_mean_game_rounds_with_ci(versions: list, mean_values: list, ci_lowers: list, ci_uppers: list, ci: int) -> None:
    """
    Plot the mean game rounds played with confidence intervals.

    Args:
        versions (list): List of version names.
        mean_values (list): List of mean game rounds played for each version.
        ci_lowers (list): List of lower bounds of the confidence intervals for each version.
        ci_uppers (list): List of upper bounds of the confidence intervals for each version.
        ci (int): Confidence interval percentage.
    """
    plt.figure(figsize=(8, 4))
    plt.bar(
        versions,
        mean_values,
        yerr=[mean_values[i] - ci_lowers[i] for i in range(len(mean_values))],
        capsize=10,
        color=["blue", "orange"],
    )
    plt.xlabel("Version")
    plt.ylabel("Mean Game Rounds Played")
    plt.title(f"Mean Game Rounds Played per Version with {ci}% CI")
    plt.show()

def plot_median_sales_with_ci(promotions: list, median_values: list, ci_lowers: list, ci_uppers: list, ci: int) -> None:
    """
    Plot the median sales with confidence intervals for each promotion.

    Args:
        promotions (list): List of promotion names.
        median_values (list): List of median sales values for each promotion.
        ci_lowers (list): List of lower bounds of the confidence intervals for each promotion.
        ci_uppers (list): List of upper bounds of the confidence intervals for each promotion.
        ci (int): Confidence interval percentage.
    """
    plt.figure(figsize=(10, 6))
    plt.errorbar(promotions, median_values, yerr=[ci_lowers, ci_uppers], fmt='o', capsize=5, capthick=2, elinewidth=2, color='blue')
    plt.title(f'Median Sales with {ci}% Confidence Intervals by Promotion')
    plt.xlabel('Promotion')
    plt.ylabel('Median Sales In Thousands')
    plt.grid(True)
    plt.show()