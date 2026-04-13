# Key Concepts — Data Analysis with Python

> **Course:** freeCodeCamp: Data Analysis with Python
> **Author:** [Your Name]
> **Last Updated:** [Date]

---

## Table of Contents

1. [NumPy — Numerical Computing](#1-numpy--numerical-computing)
2. [Pandas — Data Manipulation](#2-pandas--data-manipulation)
3. [Data Cleaning](#3-data-cleaning)
4. [Matplotlib — Core Plotting](#4-matplotlib--core-plotting)
5. [Seaborn — Statistical Visualization](#5-seaborn--statistical-visualization)
6. [SciPy — Scientific Computing](#6-scipy--scientific-computing)
7. [Descriptive Statistics Reference](#7-descriptive-statistics-reference)
8. [Challenges Overcome](#8-challenges-overcome)

---

## 1. NumPy — Numerical Computing

**Purpose:** Efficient array operations and mathematical computation on structured data.

### Array Creation & Reshaping

```python
import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
matrix = arr.reshape(3, 3)          # Reshape 1D → 3×3 matrix
flat = matrix.flatten()             # Flatten back to 1D
```

> **Key insight:** NumPy operations are *vectorized* — they apply to every element without a Python `for` loop, making them orders of magnitude faster for large datasets.

### Axis-based Operations

```python
# axis=0 → operate along rows (column-wise result)
# axis=1 → operate along columns (row-wise result)
# axis=None → operate on all elements (scalar result)

np.mean(matrix, axis=0)    # Mean of each column
np.mean(matrix, axis=1)    # Mean of each row
np.mean(matrix)            # Overall mean
```

### Common Statistical Functions

| Function | Description |
|----------|-------------|
| `np.mean(a)` | Arithmetic mean |
| `np.var(a)` | Population variance |
| `np.std(a)` | Standard deviation |
| `np.median(a)` | Median value |
| `np.max(a)` / `np.min(a)` | Maximum / Minimum |

---

## 2. Pandas — Data Manipulation

**Purpose:** Loading, exploring, filtering, grouping, and transforming tabular data.

### Loading & Inspecting Data

```python
import pandas as pd

df = pd.read_csv('data.csv')
df.head()           # First 5 rows
df.info()           # Column types and null counts
df.describe()       # Summary statistics for numeric columns
df.shape            # (rows, columns)
df.columns.tolist() # List of column names
```

### Filtering & Selection

```python
# Boolean mask filtering
df[df['age'] > 18]
df[(df['age'] > 18) & (df['country'] == 'US')]

# Select specific columns
df[['name', 'salary']]

# .loc for label-based; .iloc for integer-based
df.loc[0:5, 'age':'salary']
df.iloc[0:5, 2:5]
```

### Grouping & Aggregation

```python
# groupby → split → apply → combine
df.groupby('education')['salary'].mean()
df.groupby(['race', 'sex'])['hours-per-week'].agg(['mean', 'max', 'count'])

# Value counts — essential for categorical columns
df['occupation'].value_counts()
df['occupation'].value_counts(normalize=True)   # as proportions
```

### Common DataFrame Operations

```python
df['bmi'] = df['weight'] / (df['height'] ** 2)   # Derived column
df.drop(columns=['unnecessary_col'], inplace=True)
df.rename(columns={'old': 'new'}, inplace=True)
df.sort_values('salary', ascending=False)
df.reset_index(drop=True)
```

---

## 3. Data Cleaning

**Purpose:** Handling real-world data that is incomplete, inconsistent, or malformed.

### Handling Missing Values

```python
df.isnull().sum()                   # Count nulls per column
df.dropna()                         # Drop rows with any null
df.dropna(subset=['critical_col'])  # Drop only if specific column is null
df.fillna(df['col'].mean())         # Fill nulls with column mean
df['col'].fillna(method='ffill')    # Forward-fill
```

### Type Conversion

```python
df['age'] = df['age'].astype(int)
df['date'] = pd.to_datetime(df['date'])
df['date'].dt.year                   # Extract year from datetime
```

### Outlier Detection

```python
Q1 = df['col'].quantile(0.25)
Q3 = df['col'].quantile(0.75)
IQR = Q3 - Q1
df_clean = df[~((df['col'] < Q1 - 1.5 * IQR) | (df['col'] > Q3 + 1.5 * IQR))]
```

---

## 4. Matplotlib — Core Plotting

**Purpose:** Low-level, highly customizable chart generation.

### Figure Anatomy

```python
import matplotlib.pyplot as plt

fig, ax = plt.subplots(figsize=(10, 6))   # Always use fig, ax pattern
ax.plot(x, y, label='Trend')
ax.set_title('Title', fontsize=14)
ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.legend()
plt.tight_layout()
plt.savefig('output.png', dpi=150, bbox_inches='tight')
plt.show()
```

### Chart Types Used

```python
ax.plot(x, y)           # Line chart — trends over time
ax.bar(x, height)       # Bar chart — categorical comparison
ax.scatter(x, y)        # Scatter — correlation between variables
ax.hist(data, bins=20)  # Histogram — distribution shape
```

> **Key insight:** Always save figures *before* calling `plt.show()`. After `show()`, the figure is cleared from memory.

---

## 5. Seaborn — Statistical Visualization

**Purpose:** High-level API for statistical charts; integrates natively with Pandas DataFrames.

### Categorical Plots

```python
import seaborn as sns

# catplot — versatile, supports kind='box', 'violin', 'bar', 'strip'
sns.catplot(data=df, x='variable', y='value', col='smoke', kind='box')
```

### Heatmaps

```python
corr_matrix = df.corr()
mask = np.triu(np.ones_like(corr_matrix, dtype=bool))   # Hide upper triangle

sns.heatmap(
    corr_matrix,
    mask=mask,
    annot=True,         # Show correlation values
    fmt='.1f',          # 1 decimal place
    center=0,           # Diverging palette centered at 0
    vmin=-0.25,
    vmax=0.9
)
```

> **Key insight:** `sns.catplot()` returns a `FacetGrid` object, not an `Axes`. Use `.fig` to access the underlying figure for saving.

---

## 6. SciPy — Scientific Computing

**Purpose:** Applying statistical tests and regression models.

### Linear Regression (Sea Level Predictor)

```python
from scipy.stats import linregress

slope, intercept, r_value, p_value, std_err = linregress(x, y)

# Predict values
x_pred = pd.Series(range(1880, 2051))
y_pred = slope * x_pred + intercept

plt.plot(x_pred, y_pred, 'r--', label=f'Trend (r²={r_value**2:.3f})')
```

| Output | Meaning |
|--------|---------|
| `slope` | Rate of change per unit X |
| `intercept` | Y value when X = 0 |
| `r_value` | Correlation coefficient (−1 to 1) |
| `p_value` | Statistical significance of the slope |

---

## 7. Descriptive Statistics Reference

| Metric | Formula / Function | Interpretation |
|--------|-------------------|----------------|
| **Mean** | `sum(x) / n` | Central tendency |
| **Variance** | `mean((x - mean)²)` | Spread of data |
| **Std Dev** | `sqrt(variance)` | Spread in original units |
| **Median** | Middle value | Robust to outliers |
| **IQR** | Q3 − Q1 | Spread of middle 50% |
| **Skewness** | Asymmetry of distribution | Positive = right tail |

---

## 8. Challenges Overcome

### Challenge 1: Axis Confusion in NumPy
**Problem:** Results for row-wise vs. column-wise operations were swapped.
**Root cause:** `axis=0` collapses *rows* (produces one value per column), not the other way around.
**Solution:** Built a mental model — "axis is the dimension that *disappears*." Drew out 2D arrays on paper to verify before coding.

---

### Challenge 2: `catplot()` Returning FacetGrid Instead of Axes
**Problem:** `fig.savefig()` raised an `AttributeError` because `sns.catplot()` returns a `FacetGrid`, not an `Axes` object.
**Solution:** Accessed the underlying figure via `g = sns.catplot(...); g.fig.savefig('output.png')`.

---

### Challenge 3: Incorrect Percentage Calculations in Demographic Analysis
**Problem:** Percentages summed to over 100% because I was dividing subset counts by subset size instead of total dataset size.
**Solution:** Stored `total = len(df)` at the start and used it consistently as the denominator for all percentage calculations.

---

### Challenge 4: Datetime Indexing for Time Series
**Problem:** Filtering by year/month on a time series DataFrame raised a `TypeError` because the date column was stored as `object` (string), not `datetime64`.
**Solution:** Applied `pd.to_datetime(df['date'])` immediately after loading the CSV, then set it as the index with `df.set_index('date', inplace=True)`.

---

### Challenge 5: Linear Regression Over Two Date Ranges
**Problem:** The Sea Level Predictor required two separate regression lines — one for the full dataset and one for data from 2000 onward.
**Solution:** Filtered the DataFrame with `df[df['Year'] >= 2000]` before calling `linregress()` a second time, then plotted both prediction lines on the same axes.

---

*Document is updated as each project is completed.*