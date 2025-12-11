import pandas as pd
import numpy as np


def detect_outliers_iqr(
    df: pd.DataFrame, threshold: float = 1.5
) -> dict[str, pd.Series]:
    """
      Detects outliers in numerical columns of a DataFrame using IQR method.

    Args:
        df (pd.DataFrame): Input DataFrame containing the data.

        threshold (float): Threshold for outlier detection.
            For IQR method: Typically 1.5 (mild outliers) or 3.0 (extreme
            outliers)
    Returns:
        Dict[str, pd.Series]: Dictionary with column names as keys and Series of
            outliers as values. For columns with no outliers, an empty Series is
            returned.
    """

    numeric_df = df.select_dtypes(include=[np.number])

    if not numeric_df.columns.any():
        return {}

    q1 = numeric_df.quantile(0.25)
    q3 = numeric_df.quantile(0.75)
    iqr = q3 - q1

    lower_bound = q1 - threshold * iqr
    upper_bound = q3 + threshold * iqr

    outliers = {}
    for column in numeric_df.columns:
        mask = (numeric_df[column] < lower_bound[column]) | (
            numeric_df[column] > upper_bound[column]
        )
        outliers[column] = numeric_df[column][mask]

    return outliers


def detect_outliers_zscore(df: pd.DataFrame, threshold: float=3.0) -> dict[str, pd.Series]:
    """Detects outliers in numerical columns of a DataFrame using Z-SCORE method.

    Args:
        df (pd.DataFrame): Input DataFrame containing the data.

        threshold (float, optional): For Z-score method: Typically 3.0 (3 standard deviations)
            Defaults to 1.5.
    Returns:
        Dict[str, pd.Series]: Dictionary with column names as keys and Series of
            outliers as values. For columns with no outliers, an empty Series is
            returned.
    """
    numeric_df = df.select_dtypes(include=[np.number])

    if not numeric_df.columns.any():
        return {}

    z_scores = (numeric_df - numeric_df.mean()) / numeric_df.std()

    outliers = {}

    for column in numeric_df.columns:
        mask = abs(z_scores[column]) > threshold
        outliers[column] = numeric_df[column][mask]

    return outliers


def print_outliers(outliers: dict[str, pd.Series]) -> None:
    """Prints outliers in a formatted way.

    Args:
        outliers (Dict[str, pd.Series]): Dictionary of outliers.
    """

    for column, values in outliers.items():
        if values.empty:
            print(f"\nNo outliers in {column}")
        else:
            print(f"\nOutliers in {column}:")
            print(values)
