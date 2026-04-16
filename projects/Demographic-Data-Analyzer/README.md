# Demographic Data Analyzer
> A Python data analysis script that extracts demographic and economic insights from 1994 US Census data using Pandas — built as Project 2 of the freeCodeCamp Data Analysis with Python certification.

---

## Overview (Situation)
**Context:** 
- The 1994 US Census database contains demographic records for over 32,000 individuals, capturing attributes such as age, education, occupation, race, sex, hours worked per week, and income bracket. This kind of structured tabular data is the most common format a data analyst encounters in real-world work.

**Problem:** 
- Raw census data sitting in a CSV file tells you nothing on its own. The project required writing a program that could load, filter, group, and aggregate this data to answer 9 specific demographic and economic questions to produce precise, rounded answers that could be verified against a unit test suite.

---

## What I Built 

### Key Features
- **Race distribution** — counts total respondents per racial group using `value_counts()`, returning a ranked Pandas Series
- **Education analysis** — calculates the percentage of Bachelor's degree holders and compares the earning rates of those with and without advanced education (Bachelors, Masters, or Doctorate)
- **Work hours analysis** — identifies the minimum hours worked per week and computes what fraction of minimum-hour workers still earn above 50K
- **Country-level earnings** — calculates the percentage of high earners per country by dividing country-level salary counts and identifies the country with the highest rate
- **Occupation targeting** — filters to India-based respondents earning above 50K and identifies the most common occupation in that group

### Challenges Solved
- **Percentage calculations with the wrong denominator:** Early attempts at Q4 and Q5 divided subset counts by the total dataset length instead of the subset length, producing incorrect percentages. The fix was to compute `higher_education.sum()` and `lower_education.sum()` as the denominators — ensuring each percentage is relative to its own group, not the whole dataset.
- **Country percentage calculation with misaligned Series:** Dividing `rich_country_counts` by `country_counts` only works correctly because Pandas aligns both Series by their index (country name) before dividing. Countries appearing in one Series but not the other produce `NaN`, which `idxmax()` ignores automatically — a key Pandas behavior that avoids needing manual filtering.

---

## Results and Impact
- All 10 unit tests passing with 0 errors
- Correctly identifies Iran as the country with the highest percentage of earners above 50K at 41.9%
- Correctly identifies Prof-specialty as the most popular occupation for high earners in India
- All decimal values rounded to 1 decimal place as required by the specification

---

## Getting Started

```bash
git clone https://github.com/MarlanAlfonso/boilerplate-demographic-data-analyzer.git
pip install pandas
python3 main.py
```

### Example Output

```
Number of each race:
 White                 27816
 Black                  3124
 Asian-Pac-Islander     1039
 Amer-Indian-Eskimo      311
 Other                   271

Average age of men: 39.4
Percentage with Bachelors degrees: 16.4%
Percentage with higher education that earn >50K: 46.5%
Percentage without higher education that earn >50K: 17.4%
Min work time: 1 hours/week
Percentage of rich among those who work fewest hours: 10.0%
Country with highest percentage of rich: Iran
Highest percentage of rich people in country: 41.9%
Top occupations in India: Prof-specialty
```

---

## What I Learned
- Learned how to use `.isin()` to filter rows where a column value matches any item in a list — essential for grouping education levels into broad categories
- Understood how Pandas aligns Series by index during arithmetic operations, which enables dividing two differently-sized Series by country name without a manual join
- Gained experience with `.value_counts()`, `.idxmax()`, and boolean indexing as the core toolkit for categorical data analysis
- Practiced chaining multiple filters — `df[(df['native-country'] == 'India') & (df['salary'] == '>50K')]` — to drill into specific population subsets
- Understood the importance of choosing the correct denominator in percentage calculations: dividing by subset size vs. total dataset size produces completely different and potentially misleading results
