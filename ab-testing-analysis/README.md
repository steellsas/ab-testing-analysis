# 📊 A/B Testing Analysis

[![Python](https://img.shields.io/badge/Python-3.11-blue.svg)](https://python.org)
[![Pandas](https://img.shields.io/badge/Pandas-2.0-green.svg)](https://pandas.pydata.org)
[![SciPy](https://img.shields.io/badge/SciPy-Statistics-orange.svg)](https://scipy.org)
[![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-F37626.svg)](https://jupyter.org)

A collection of A/B testing case studies demonstrating statistical analysis techniques for business decision-making. This repository contains two comprehensive analyses: a mobile game engagement study and a marketing campaign effectiveness evaluation.

---

## 📋 Table of Contents

- [Overview](#-overview)
- [Projects](#-projects)
  - [Cookie Cats Game Analysis](#-cookie-cats-game-analysis)
  - [Marketing Campaign Analysis](#-marketing-campaign-analysis)
- [Statistical Methods](#-statistical-methods)
- [Key Findings Summary](#-key-findings-summary)
- [Tech Stack](#-tech-stack)
- [Project Structure](#-project-structure)
- [Installation](#-installation)
- [Usage](#-usage)

---

## 🎯 Overview

This repository demonstrates end-to-end A/B testing workflows including:

- **Hypothesis formulation** with clear H₀ and Hₐ definitions
- **Data cleaning** and preprocessing with outlier handling
- **Assumption testing** (normality, homogeneity of variance)
- **Statistical testing** using both parametric and non-parametric methods
- **Effect size calculation** with bootstrap confidence intervals
- **Business recommendations** based on statistical evidence

---

## 📁 Projects

### 🎮 Cookie Cats Game Analysis

**Business Question:** Does moving the first gate from level 30 to level 40 increase player engagement?

| Metric | Gate 30 | Gate 40 | Difference |
|--------|---------|---------|------------|
| **Median Rounds** | 72 | 92 | +27.8% |
| **Mean Rounds** | 122.1 | 142.7 | +16.9% |
| **1-Day Retention** | 80.1% | 83.0% | +2.9pp |
| **7-Day Retention** | 43.9% | 48.5% | +4.6pp |

**Statistical Tests:**
- Shapiro-Wilk (normality): p < 0.001 → Non-normal distribution
- Mann-Whitney U test: p < 0.001 → Significant difference
- Bootstrap 95% CI: No overlap between groups

**Conclusion:** 🏆 **Gate 40 significantly outperforms Gate 30.** Players who encounter the gate at level 40 play approximately 17% more game rounds on average.

**Recommendation:** Move the gate to level 40 to increase player engagement.

---

### 📈 Marketing Campaign Analysis

**Business Question:** Which of three marketing promotions generates the highest sales for a new menu item?

| Metric | Promotion 1 | Promotion 2 | Promotion 3 |
|--------|-------------|-------------|-------------|
| **Median Sales (K)** | 55.4 | 45.4 | 51.2 |
| **Mean Sales (K)** | 58.1 | 47.3 | 55.4 |
| **Std Dev** | 16.6 | 15.1 | 16.8 |

**Statistical Tests:**
- Shapiro-Wilk (normality): p < 0.001 → Non-normal distribution
- Kruskal-Wallis H-test: p < 0.001 → Significant differences exist
- Post-hoc Dunn's test (Bonferroni corrected):
  - P1 vs P2: p < 0.001 ✅ Significant
  - P3 vs P2: p < 0.001 ✅ Significant
  - P1 vs P3: p = 0.146 ❌ Not significant

**Effect Sizes (Median Difference):**
| Comparison | Difference | 95% CI | Interpretation |
|------------|------------|--------|----------------|
| P1 vs P2 | +10.0K | [7.0, 12.3] | P1 ~22% better |
| P3 vs P2 | +5.9K | [3.5, 7.9] | P3 ~13% better |
| P1 vs P3 | +4.2K | [1.5, 6.6] | Similar performance |

**Conclusion:** 🏆 **Promotion 1 is the most effective overall.** Promotion 2 significantly underperforms and should be discontinued.

**Recommendation:** Implement Promotion 1 for the new menu item launch. Consider Promotion 3 as an alternative in large markets where it shows strong performance.

---

## 📐 Statistical Methods

### Methodology Comparison

| Aspect | Cookie Cats | Marketing Campaign |
|--------|-------------|-------------------|
| **Groups** | 2 (A/B) | 3 (A/B/C) |
| **Sample Size** | ~30,000 | ~550 |
| **Primary Test** | Mann-Whitney U | Kruskal-Wallis H |
| **Post-hoc** | N/A | Dunn's test |
| **Effect Size** | Bootstrap Mean CI | Bootstrap Median CI |
| **Correction** | N/A | Bonferroni |

### Statistical Testing Framework

```
┌─────────────────────────────────────────────────────────────┐
│                    DATA COLLECTION                           │
└─────────────────────────┬───────────────────────────────────┘
                          ▼
┌─────────────────────────────────────────────────────────────┐
│              ASSUMPTION TESTING                              │
│  • Shapiro-Wilk (Normality)                                 │
│  • Levene's Test (Homogeneity of Variance)                  │
│  • Sample Ratio Mismatch Check                              │
└─────────────────────────┬───────────────────────────────────┘
                          ▼
            ┌─────────────┴─────────────┐
            ▼                           ▼
┌───────────────────────┐   ┌───────────────────────┐
│   NORMAL DATA         │   │   NON-NORMAL DATA     │
│   • T-test (2 groups) │   │   • Mann-Whitney U    │
│   • ANOVA (3+ groups) │   │   • Kruskal-Wallis H  │
└───────────┬───────────┘   └───────────┬───────────┘
            └─────────────┬─────────────┘
                          ▼
┌─────────────────────────────────────────────────────────────┐
│              POST-HOC ANALYSIS (if needed)                   │
│  • Dunn's Test with Bonferroni correction                   │
│  • Bootstrap Confidence Intervals                            │
│  • Effect Size Calculation                                   │
└─────────────────────────┬───────────────────────────────────┘
                          ▼
┌─────────────────────────────────────────────────────────────┐
│              BUSINESS RECOMMENDATION                         │
└─────────────────────────────────────────────────────────────┘
```

### Key Statistical Concepts Applied

| Concept | Description | Application |
|---------|-------------|-------------|
| **Type I Error (α)** | False positive rate | Set at 0.05 (95% confidence) |
| **Type II Error (β)** | False negative rate | Power analysis for sample size |
| **Bonferroni Correction** | Multiple comparison adjustment | α/n for post-hoc tests |
| **Bootstrap Resampling** | Non-parametric CI estimation | 10,000 iterations |
| **Effect Size** | Practical significance | Median/mean differences |

---

## 🔑 Key Findings Summary

### Cookie Cats Game
| Finding | Impact |
|---------|--------|
| Gate position significantly affects engagement | ✅ Confirmed |
| Gate 40 increases game rounds by ~17% | High impact |
| Gate 40 improves 7-day retention by 4.6pp | Medium impact |
| **Recommendation** | Move gate to level 40 |

### Marketing Campaign
| Finding | Impact |
|---------|--------|
| Promotions have significantly different effects | ✅ Confirmed |
| Promotion 1 generates ~22% more sales than P2 | High impact |
| Promotion 1 and 3 perform similarly overall | Low difference |
| P3 excels in large markets (median: 82.3K) | Segment-specific |
| **Recommendation** | Implement Promotion 1 |

---

## 🛠️ Tech Stack

| Category | Tools |
|----------|-------|
| **Language** | Python 3.11 |
| **Data Processing** | Pandas, NumPy |
| **Statistical Analysis** | SciPy, statsmodels, scikit-posthocs |
| **Visualization** | Matplotlib, Seaborn |
| **Environment** | Jupyter Notebook |

---

## 📁 Project Structure

```
ab-testing-analysis/
├── cookie_cats_game/
│   ├── data/
│   │   └── cookie_cats.csv
│   ├── utils/
│   │   ├── eda_utils.py
│   │   ├── stats_utils.py
│   │   └── utils.py
│   ├── game_A_B_analysis.ipynb
│   └── README.md
├── marketing_campaign/
│   ├── data/
│   │   └── WA_Marketing-Campaign.csv
│   ├── utils/
│   │   ├── eda_utils.py
│   │   ├── stats_utils.py
│   │   └── utils.py
│   ├── marketing_A_B_analysis.ipynb
│   └── README.md
├── README.md
├── requirements.txt
└── .gitignore
```

---

## 💻 Installation

### Prerequisites

- Python 3.9+
- Jupyter Notebook or JupyterLab

### Setup

```bash
# Clone the repository
git clone https://github.com/yourusername/ab-testing-analysis.git
cd ab-testing-analysis

# Create virtual environment
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### Requirements

```txt
numpy>=1.24.0
pandas>=2.0.0
matplotlib>=3.7.0
seaborn>=0.12.0
scipy>=1.10.0
statsmodels>=0.14.0
scikit-posthocs>=0.7.0
jupyter>=1.0.0
```

---

## 🚀 Usage

### Running the Analyses

```bash
# Cookie Cats Game Analysis
cd cookie_cats_game
jupyter notebook game_A_B_analysis.ipynb

# Marketing Campaign Analysis
cd marketing_campaign
jupyter notebook marketing_A_B_analysis.ipynb
```

### Using the Utility Functions

```python
# Statistical utilities
from utils.stats_utils import bootstrap_median_ci, bootstrap_mean_ci

# Calculate confidence interval
median_val, ci_lower, ci_upper = bootstrap_median_ci(data, ci=95)
print(f"Median: {median_val:.2f}, 95% CI: [{ci_lower:.2f}, {ci_upper:.2f}]")

# Plotting utilities
from utils.utils import plot_promotion_distributions, draw_boxplot

# Create visualizations
plot_promotion_distributions(df)
draw_boxplot(data=df, x='group', y='value')
```

---

## 📚 References

- [A/B Testing - The Definitive Guide](https://www.optimizely.com/optimization-glossary/ab-testing/)
- [Statistical Methods in Online A/B Testing](https://towardsdatascience.com/statistical-methods-in-online-a-b-testing-9e28b6bf2e8d)
- [Cookie Cats Dataset - Kaggle](https://www.kaggle.com/datasets/mursideyarkin/mobile-games-ab-testing-cookie-cats)
- [Marketing Campaign Dataset - IBM Watson Analytics](https://www.ibm.com/communities/analytics/watson-analytics/)

---

## 📄 License

This project is for educational and portfolio purposes.

---

## 👤 Author

**Andrius**

- GitHub: [@steellsas](https://github.com/steellsas)
