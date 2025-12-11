# Stats functions
"""
A collection of statistical utility functions for hypothesis testing, confidence
interval estimation, bootstrap resampling, etc.
"""
import numpy as np
import pandas as pd
from scipy.stats import ttest_ind

def perform_t_tests(df, group_col, value_col):
    """
    Perform t-tests between all unique pairs of groups in the dataframe.

    Parameters:
    -----------
    df : pd.DataFrame
        DataFrame containing the data.
    group_col : str
        Column name for the groups.
    value_col : str
        Column name for the values to be tested.

    Returns:
    --------
    results : dict
        Dictionary with t-statistics and p-values for each pair of groups.
    """
    groups = df[group_col].unique()
    results = {}
    
    for i in range(len(groups)):
        for j in range(i + 1, len(groups)):
            group1 = df[df[group_col] == groups[i]][value_col]
            group2 = df[df[group_col] == groups[j]][value_col]
            
            t_stat, p_value = ttest_ind(group1, group2)
            results[f'{groups[i]} vs {groups[j]}'] = {'t_stat': t_stat, 'p_value': p_value}
    
    return results

def bootstrap_median_ci(group: pd.Series, ci: int, n_bootstraps: int = 1000) -> tuple[float, float, float]:
    """
    Calculate the median value and confidence interval using bootstrapping.

    Parameters:
    -----------
    group : array-like
        Data for the group.
    n_bootstraps : int
        Number of bootstrap samples.
    ci : int
        Confidence level (e.g., 95 for 95% CI).

    Returns:
    --------
    median_value : float
        Median value of a group.
    ci_lower : float
        Lower bound of the confidence interval.
    ci_upper : float
        Upper bound of the confidence interval.
    """
    bootstrap_median = []
    for _ in range(n_bootstraps):
        resampled = group.sample(len(group), replace=True)
        bootstrap_median.append(np.median(resampled))
    median_val = np.median(bootstrap_median)
    ci_lower = np.percentile(bootstrap_median, (100 - ci) / 2)
    ci_upper = np.percentile(bootstrap_median, 100 - ((100 - ci) / 2))

    return median_val, ci_lower, ci_upper

def bootstrap_median_difference_ci(group1: pd.Series, group2: pd.Series, ci: int, n_bootstraps: int = 1000) -> tuple[float, float, float]:
    """
    Calculate the median difference and confidence interval using bootstrapping.

    Parameters:
    -----------
    group1, group2 : array-like
        Data for the two groups.
    ci : int
        Confidence level (e.g., 95 for 95% CI).
    n_bootstraps : int
        Number of bootstrap samples.

    Returns:
    --------
    median_diff : float
        Median difference between the two groups.
    ci_lower : float
        Lower bound of the confidence interval.
    ci_upper : float
        Upper bound of the confidence interval.
    """
    bootstrap_differences = []
    for _ in range(n_bootstraps):
        resample1 = group1.sample(len(group1), replace=True)
        resample2 = group2.sample(len(group2), replace=True)
        bootstrap_differences.append(np.median(resample1) - np.median(resample2))
    ci_lower = np.percentile(bootstrap_differences, (100 - ci) / 2)
    ci_upper = np.percentile(bootstrap_differences, 100 - ((100 - ci) / 2))
    median_diff = np.median(bootstrap_differences)

    return median_diff, ci_lower, ci_upper
