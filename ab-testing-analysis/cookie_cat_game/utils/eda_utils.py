import pandas as pd
import numpy as np


def check_missing_values(df):
    """
    Checks for missing values in the DataFrame.

    Parameters:
    df (DataFrame): The DataFrame to check.

    Returns:
    None
    """
    missing_values = df.isnull().sum()
    if missing_values.any():
        print("Missing values found:")
        print(missing_values[missing_values > 0])
    else:
        print("The dataset does not contain any missing values.")

def check_duplicates(df, column_names=None):
    """
    Checks for duplicate rows in the DataFrame.

    Parameters:
    df (DataFrame): The DataFrame to check.
    column_names (list): The list of column names to check for duplicates.

    Returns:
    None
    """
    if column_names:
        duplicates = df.duplicated(subset=column_names)
    else:
        duplicates = df.duplicated()
    if duplicates.any():
        print(f"Duplicate rows found based on the columns: {column_names}")
    else:
        print(f"No duplicate rows found based on the columns: {column_names}")

def find_outlier_rows_by_iqr(df: pd.DataFrame, columns: list = None) -> pd.DataFrame:
    """
    Identify and return rows in a DataFrame that contain outliers based on the
    Interquartile Range (IQR) method.

    Parameters:
    ----------
    df : pd.DataFrame
        The input DataFrame containing the data to analyze for outliers.
    columns : list, optional
        A list of column names to check for outliers. If None (default), the function
        will analyze all numerical columns (int64 and float64).

    Returns:
  
    pd.DataFrame
        A DataFrame containing only the rows from the original DataFrame that are
        identified as having outliers in any of the specified columns.
    """
    if columns is None:
        columns = df.select_dtypes(include=["int64", "float64"]).columns.tolist()
    outlier_mask = pd.Series(False, index=df.index)

    for col in columns:
        Q1 = df[col].quantile(0.25)
        Q3 = df[col].quantile(0.75)
        IQR = Q3 - Q1

        lower_bound = Q1 - 1.5 * IQR
        upper_bound = Q3 + 1.5 * IQR
        col_outlier_mask = (df[col] < lower_bound) | (df[col] > upper_bound)
        outlier_mask |= col_outlier_mask

    return df[outlier_mask]