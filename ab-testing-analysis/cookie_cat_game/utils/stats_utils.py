"""
Calculate the bootstrap mean and confidence interval for a given data group.
Parameters:
group (array-like): The data group to sample from.
sample_size (int): The size of each bootstrap sample.
ci (float, optional): The confidence interval percentage. Default is 95.
n_bootstrap (int, optional): The number of bootstrap samples to generate. Default is 1000.
Returns:
tuple: A tuple containing the mean of the bootstrap samples, the lower bound of the confidence interval, 
       and the upper bound of the confidence interval.
"""
import numpy as np

def bootstrap_mean_ci(group, sample_size, ci=95, n_bootstraps=1000):
    """
    Calculates the bootstrap mean and confidence interval for a given group.

    Parameters:
    group (Series): The data to bootstrap.
    sample_size (int): The size of each bootstrap sample.
    ci (int): The confidence interval percentage.
    n_bootstraps (int): The number of bootstrap samples to generate.

    Returns:
    tuple: The mean, lower bound, and upper bound of the confidence interval.
    """
    bootstrapped_means = []
    for _ in range(n_bootstraps):
        sample = np.random.choice(group, size=sample_size, replace=True)
        bootstrapped_means.append(np.mean(sample))
    mean = np.mean(bootstrapped_means)
    lower_bound = np.percentile(bootstrapped_means, (100 - ci) / 2)
    upper_bound = np.percentile(bootstrapped_means, 100 - (100 - ci) / 2)
    return mean, lower_bound, upper_bound
