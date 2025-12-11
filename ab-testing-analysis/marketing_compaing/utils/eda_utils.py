import pandas as pd
import numpy as np

def check_missing_values(df: pd.DataFrame) -> None:
    """
    Checks for missing values in the given DataFrame and prints the results.

    Parameters
    ----------
    df : pd.DataFrame
        The DataFrame to be checked for missing values.
    """
    if df.isna().values.any():
        print("Missing value counts by column:")
        print(df.isna().sum())
    else:
        print("The dataset does not contain any missing values.")


def check_duplicates(df: pd.DataFrame, column_names: list = None) -> pd.DataFrame:
    """
    Checks for duplicate rows in the DataFrame based on the specified column names.
    If no column names are provided, checks for duplicates across the entire DataFrame.

    Parameters
    ----------
    df : pd.DataFrame
        The DataFrame to be checked for duplicates.
    column_names : list, optional
        List of column names to check for duplicates. Defaults to None, meaning full
        rows will be checked.

    Returns
    -------
    pd.DataFrame
        A DataFrame containing the duplicate rows. If no duplicates are found,
        an empty DataFrame is returned.
    """
    if column_names is None:
        column_names = df.columns.tolist()

    duplicate_rows = df[df.duplicated(subset=column_names, keep=False)]

    if not duplicate_rows.empty:
        print(
            f"There are {len(duplicate_rows)} duplicate rows based on the columns: "
            f"{column_names}"
        )
        return duplicate_rows
    else:
        print(f"No duplicate rows found based on the columns: {column_names}")


def check_inconsistent_spaces_capitalization(
    df: pd.DataFrame, categorical_columns: list[str]
) -> str:
    """
    Checks and fixes inconsistencies in categorical columns caused by extra spaces
    or differences in capitalization.

    Parameters
    ----------
    df : pd.DataFrame
        The input DataFrame to be checked for inconsistencies.
    categorical_columns : list of str
        List of column names to be processed for inconsistencies.

    Returns
    -----
        A message informing on inconsistencies found and fixed in DataFrame, if any.
    """
    inconsistent_columns = 0
    for column in categorical_columns:
        len_og_column = len(df[column].unique())
        processed_column = df[column].str.lower().str.strip()
        len_stripped_column = len(processed_column.unique())
        if len_og_column != len_stripped_column:
            print(
                f"After stripping and decapitalization: {len_stripped_column} unique"
                f" values instead of {len_og_column}."
            )
            df[column] = processed_column
            inconsistent_columns += 1

    if not inconsistent_columns:
        return (
            "There are no inconsistent - extra spaces and or different capitalization -"
            + " data entries in categorical columns."
        )
    else:
        return (
            "Inconsistencies were fixed, but this also indicates there might "
            + "be other inconsistencies due to e.g. misspelling."
        )


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