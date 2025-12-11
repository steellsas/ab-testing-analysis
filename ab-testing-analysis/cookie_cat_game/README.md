# Mobile Games A/B Testing - Cookie Cats

## Introduction

This project analyzes the results of an A/B test conducted in the mobile game Cookie Cats. The goal is to evaluate the impact of changing the placement of the first gate in the game on player engagement, measured by the total number of game rounds played during the first 14 days after installation.

## Dataset

The dataset contains the following columns:

- `userid`: A unique number that identifies each player.
- `version`: Indicates whether the player was in the control group (gate_30) or the treatment group (gate_40).
- `sum_gamerounds`: The number of game rounds played by the player during the first 14 days after installation.
- `retention_1`: Whether the player returned to play 1 day after installing the game.
- `retention_7`: Whether the player returned to play 7 days after installing the game.

## Analysis

The analysis includes:

1. Data Cleaning and Preprocessing
2. Exploratory Data Analysis
3. A/B Testing to compare the two versions of the game

## Key Findings

- **Retention Rates**: The overall 1-day retention rate is approximately 46.5%, and the 7-day retention rate is around 19.4%.
- **Group Comparison**: Both groups have similar retention rates, with gate_30 showing slightly better performance.
- **Statistical Significance**: The Mann-Whitney U test indicated a statistically significant difference between the two groups, suggesting that the gate_30 version may be preferable.

## Conclusion

The analysis indicates that the gate_30 version of the game might be more beneficial for player engagement compared to the gate_40 version. The statistical tests conducted show a significant difference between the two groups, suggesting that players in the gate_30 group tend to play more game rounds on average.

## Future Improvements

1. **Longer Observation Period**: Extend the observation period beyond 14 days to capture long-term player engagement and retention.
2. **Additional Metrics**: Include other metrics such as in-game purchases, player progression, and churn rate to provide a more comprehensive analysis.
3. **Segment Analysis**: Perform segmentation analysis to understand how different player demographics respond to the gate changes.
4. **A/B Testing Variations**: Conduct additional A/B tests with different gate positions (e.g., level 35) to find the optimal gate placement.
5. **Player Feedback**: Collect qualitative feedback from players to understand their preferences and pain points related to gate placement.

## How to Run the Analysis

1. Clone the repository:

    ```bash
    git clone <repository-url>
    ```

2. Navigate to the project directory:

    ```bash
    cd /c:/Users/steel/turing_projects/A_B_tests/anplien-DS.v3.2.2.5
    ```

3. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. Open the Jupyter Notebook:

    ```bash
    jupyter notebook game_A_B_analysis.ipynb
    ```

5. Run the cells in the notebook to perform the analysis.