
# Marketing Campaign Analysis

This module contains utilities for analyzing marketing campaign data, including statistical tests, plotting functions, and outlier detection.

## Directory Structure

- `utils/`
  - `stats_utils.py`: Contains statistical utility functions for hypothesis testing, confidence interval estimation, and bootstrap resampling.
  - `utils.py`: Contains utility functions for plotting and outlier detection.

## Installation

To use the utilities in this module, you need to have the following Python packages installed:

- `numpy`
- `pandas`
- `matplotlib`
- `seaborn`
- `scipy`

You can install these packages using pip:

```bash
pip install numpy pandas matplotlib seaborn scipy
```

## Usage

### Statistical Utilities

#### `perform_t_tests`

Performs t-tests between all unique pairs of groups in a DataFrame.

```python
from utils.stats_utils import perform_t_tests

results = perform_t_tests(df, group_col='Group', value_col='Value')
print(results)
```

#### `bootstrap_median_ci`

Calculates the median value and confidence interval using bootstrapping.

```python
from utils.stats_utils import bootstrap_median_ci

median_val, ci_lower, ci_upper = bootstrap_median_ci(group, ci=95, n_bootstraps=1000)
print(median_val, ci_lower, ci_upper)
```

#### `bootstrap_median_difference_ci`

Calculates the median difference and confidence interval between two groups using bootstrapping.

```python
from utils.stats_utils import bootstrap_median_difference_ci

median_diff, ci_lower, ci_upper = bootstrap_median_difference_ci(group1, group2, ci=95, n_bootstraps=1000)
print(median_diff, ci_lower, ci_upper)
```

### Plotting Utilities

#### `draw_histplot`

Creates a histogram plot showing the distribution of data.

```python
from utils.utils import draw_histplot

draw_histplot(data, title='Histogram', x_label='Value', y_label='Frequency')
```

#### `draw_barplot`

Creates a bar plot.

```python
from utils.utils import draw_barplot

draw_barplot(x, y, title='Bar Plot', x_label='Category', y_label='Value')
```

#### `draw_countplot`

Creates a count plot.

```python
from utils.utils import draw_countplot

draw_countplot(data, title='Count Plot', x_label='Category', y_label='Count')
```

#### `draw_boxplot`

Creates a box plot.

```python
from utils.utils import draw_boxplot

draw_boxplot(data, title='Box Plot', x_label='Category', y_label='Value')
```

#### `plot_promotion_distributions`

Plots the distribution of sales for different promotions.

```python
from utils.utils import plot_promotion_distributions

plot_promotion_distributions(data)
```

#### `plot_sales_distribution`

Plots the distribution of sales using a histogram and a box plot.

```python
from utils.utils import plot_sales_distribution

plot_sales_distribution(data)
```

#### `draw_gates_plot`

Plots histograms and box plots for different gates.

```python
from utils.utils import draw_gates_plot

draw_gates_plot(df, column='Value', group_col='Gate')
```

#### `plot_mean_game_rounds_with_ci`

Plots the mean game rounds played with confidence intervals.

```python
from utils.utils import plot_mean_game_rounds_with_ci

plot_mean_game_rounds_with_ci(versions, mean_values, ci_lowers, ci_uppers, ci=95)
```

#### `plot_median_sales_with_ci`

Plots the median sales with confidence intervals for each promotion.

```python
from utils.utils import plot_median_sales_with_ci

plot_median_sales_with_ci(promotions, median_values, ci_lowers, ci_uppers, ci=95)
```

### Outlier Detection

#### `get_outliers_mask_iqr`

Detects outliers in a pandas series using the IQR method.

```python
from utils.utils import get_outliers_mask_iqr

outliers_mask = get_outliers_mask_iqr(data)
print(outliers_mask)
```

## License

This project is licensed under the MIT License.
