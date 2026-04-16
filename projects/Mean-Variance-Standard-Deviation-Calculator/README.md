# Mean-Variance-Standard Deviation Calculator

> A Python function that computes descriptive statistics on a 3x3 matrix — built as Project 1 of the freeCodeCamp Data Analysis with Python.

---

## Overview (Situation)

**Context:** 
- Descriptive statistics — mean, variance, standard deviation, min, max, and sum are the foundation of every data analysis workflow. Understanding how these metrics behave across different axes of a matrix is essential before working with larger datasets using libraries like Pandas and NumPy.

**Problem:** 
- The project required building a function that could take a flat list of 9 numbers, restructure it into a matrix, and return all six statistical measures computed three ways: column-wise, row-wise, and across all elements in a single, structured output.

---

## What I Built (Action)

### Key Features

- **Input validation** — raises a `ValueError` with a descriptive message if the input list contains fewer than 9 elements, preventing silent failures downstream
- **Matrix reshaping** — converts a 1D list into a 3x3 NumPy array using `reshape(3, 3)`, enabling axis-based operations
- **Axis-aware statistics** — computes every metric along `axis=0` (column-wise), `axis=1` (row-wise), and on the flattened array, returning all results in one structured dictionary
- **Clean output format** — all NumPy arrays are converted to plain Python lists using `.tolist()` so the output is JSON-serializable and test-compatible

### Tech Stack

| Layer | Technology |
|---|---|
| Language | Python 3 |
| Numerical Computing | NumPy |
| Testing | unittest (freeCodeCamp test suite) |
| Environment | GitHub Codespaces |

### Challenges Solved

**Axis confusion — column-wise vs. row-wise:** NumPy's `axis` parameter is counterintuitive at first. `axis=0` collapses rows and produces one value per column, while `axis=1` collapses columns and produces one value per row. I resolved this by mentally modeling the axis as "the dimension that disappears" and verifying each result against the expected output manually before running the test suite.

**Output type mismatch — NumPy arrays vs. Python lists:** NumPy statistical functions return `ndarray` objects, not plain Python lists. The unit tests expected native Python types, so every result required `.tolist()` to convert — including scalar values returned from the flattened computation.

---

## Results and Impact

- All 3 unit tests passing with 0 errors
- Function handles both valid input and edge cases (under-length lists) correctly
- Output matches the exact format specified by freeCodeCamp across all 6 statistical measures and 3 axis configurations
- Completed and submitted as a verified project toward the Data Analysis with Python certification

---

## Getting Started

```bash
git clone https://github.com/MarlanAlfonso/boilerplate-mean-variance-standard-deviation-calculator.git
cd boilerplate-mean-variance-standard-deviation-calculator
pip install numpy
python3 main.py
```

### Expected Output

```python
{
  'mean': [[3.0, 4.0, 5.0], [1.0, 4.0, 7.0], 4.0],
  'variance': [[6.0, 6.0, 6.0], [0.667, 0.667, 0.667], 6.667],
  'standard deviation': [[2.449, 2.449, 2.449], [0.816, 0.816, 0.816], 2.582],
  'max': [[6, 7, 8], [2, 5, 8], 8],
  'min': [[0, 1, 2], [0, 3, 6], 0],
  'sum': [[9, 12, 15], [3, 12, 21], 36]
}
```

---

## What I Learned

- Understood how NumPy's `axis` parameter controls the direction of statistical operations — `axis=0` for column-wise, `axis=1` for row-wise, and no axis for the full array
- Learned that `reshape()` requires the total element count to stay constant — reshaping 9 elements into anything other than a 1x9, 3x3, or 9x1 matrix raises an error
- Gained hands-on experience with NumPy's core statistical functions: `np.mean()`, `np.var()`, `np.std()`, `np.max()`, `np.min()`, `np.sum()`
- Practiced writing Python `ValueError` exceptions for input validation — a pattern used throughout production data pipelines to catch bad data early
- Learned that `.tolist()` is required to convert NumPy output to plain Python types, which matters for JSON serialization and test compatibility