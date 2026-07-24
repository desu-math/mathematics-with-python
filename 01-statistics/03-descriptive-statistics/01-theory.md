# Descriptive Statistics

## Overview

Descriptive statistics is the branch of statistics that focuses on **organizing, summarizing, and describing data**.

Rather than drawing conclusions about a population, descriptive statistics helps us understand the characteristics of the data we have collected.

By using numerical measures and graphical representations, descriptive statistics transforms raw data into meaningful information that is easier to interpret.

---

# Objectives of Descriptive Statistics

The main objectives of descriptive statistics are to:

* summarize large datasets,
* identify patterns and trends,
* measure the center of the data,
* measure the spread of the data,
* detect unusual observations,
* present data in a clear and understandable form.

---

# Main Components of Descriptive Statistics

Descriptive statistics is commonly divided into three major components:

1. Measures of Central Tendency
2. Measures of Dispersion
3. Data Visualization

---

# 1. Measures of Central Tendency

Measures of central tendency describe the **typical or central value** of a dataset.

The most common measures are:

* Mean
* Median
* Mode

These measures provide different ways of representing the "center" of the data.

---

## Mean

The **mean** (average) is obtained by dividing the sum of all observations by the number of observations.

It is the most widely used measure of central tendency but can be influenced by extreme values (outliers).

---

## Median

The **median** is the middle value of an ordered dataset.

If the dataset contains an even number of observations, the median is the average of the two middle values.

Unlike the mean, the median is less affected by outliers.

---

## Mode

The **mode** is the value that occurs most frequently in a dataset.

A dataset may have:

* one mode (unimodal),
* two modes (bimodal),
* multiple modes (multimodal),
* or no mode if all values occur with the same frequency.

---

# 2. Measures of Dispersion

Measures of dispersion describe **how spread out the data is**.

Two datasets may have the same mean but very different variability.

Common measures include:

* Range
* Variance
* Standard Deviation
* Interquartile Range (IQR)

---

## Range

The range is the difference between the largest and smallest observations.

It provides a simple measure of the total spread of the data.

---

## Variance

Variance measures the average squared deviation of observations from the mean.

A larger variance indicates greater variability.

---

## Standard Deviation

The standard deviation is the square root of the variance.

Because it has the same unit as the original data, it is easier to interpret than variance.

It is one of the most commonly used measures of variability.

---

## Interquartile Range (IQR)

The interquartile range measures the spread of the middle 50% of the data.

It is calculated as:

```text id="jrbffq"
IQR = Q3 − Q1
```

where:

* **Q1** is the first quartile.
* **Q3** is the third quartile.

The IQR is resistant to outliers and is commonly used in box plots.

---

# 3. Data Visualization

Graphical representations help reveal patterns that may not be obvious from numerical summaries alone.

Common visualizations include:

* Histogram: used for continuous numerical data.
* Bar Chart: used to compare categories.
* Pie Chart: used to shows parts of a whole.
* Box Plot: used to summarizes a distribution using: Minimum, First quartile (Q1), Median, Third quartile (Q3),Maximum.
* Scatter Plot: used to shows the relationship between two numerical variables.

```text
  Chart selection guide:

  Do I have categories?
        │
        ├── Yes
        │      │
        │      ├── Compare counts → Bar Chart
        │      │
        │      └── Show percentages → Pie Chart
        │
        └── No (Numerical Data)
               │
               ├── Show distribution → Histogram
               │
               ├── Show change over time → Line Chart
               │
               ├── Compare two numerical variables → Scatter Plot
               │
               └── Compare spread or detect outliers → Box Plot

Visualization is an essential part of exploratory data analysis.
```
---

# Why Descriptive Statistics Matters

Descriptive statistics is usually the **first step** in any data analysis project.

Before building predictive models or performing statistical inference, analysts first explore and summarize the available data.

This process helps identify:

* the overall distribution,
* central values,
* variability,
* missing values,
* potential outliers,
* unusual patterns.

---

# Python and Descriptive Statistics

Python provides powerful libraries for descriptive statistical analysis.

Commonly used libraries include:

* **NumPy** for numerical computations.
* **Pandas** for dataset manipulation.
* **Matplotlib** for visualization.

These libraries allow efficient analysis of datasets ranging from a few observations to millions of records.

---

# Summary

* Descriptive statistics summarizes and describes data.
* Its three main components are:

  * Measures of Central Tendency,
  * Measures of Dispersion,
  * Data Visualization.
* Central tendency describes the typical value of a dataset.
* Dispersion measures the variability of the data.
* Visualization helps identify patterns and communicate results effectively.
* Descriptive statistics forms the foundation of exploratory data analysis and many data science workflows.
