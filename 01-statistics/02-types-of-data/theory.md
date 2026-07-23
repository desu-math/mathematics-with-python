# Types of Data

## Overview

Before analyzing data, it is important to understand its type.

Different types of data require different statistical methods, visualizations, and machine learning algorithms. Correctly identifying the data type is the first step in any statistical analysis.

---

# Classification of Data

Data can be classified in several ways. The two most common classifications are:

* By nature of the data
* By measurement scale

---

# Classification by Nature

## 1. Qualitative (Categorical) Data

Qualitative data describes **qualities, categories, or labels** rather than numerical values.

Examples:

* Gender
* Blood type
* Eye color
* Country
* Soil type

Qualitative data is usually divided into categories and cannot be meaningfully added, subtracted, multiplied, or divided.

---

## 2. Quantitative (Numerical) Data

Quantitative data represents **numerical values** that can be measured or counted.

Examples:

* Age
* Height
* Weight
* Temperature
* Income
* Exam score

Quantitative data supports mathematical operations and statistical calculations.

---

# Types of Quantitative Data

## Discrete Data

Discrete data consists of **countable values**.

Characteristics:

* Takes distinct values.
* Usually whole numbers.
* Obtained by counting.

Examples:

* Number of students
* Number of books
* Number of cars
* Number of customers

---

## Continuous Data

Continuous data consists of **measurable values**.

Characteristics:

* Can take any value within an interval.
* May contain decimal values.
* Obtained by measurement.

Examples:

* Height
* Weight
* Time
* Distance
* Temperature

---

# Classification by Measurement Scale

## 1. Nominal Scale

The nominal scale classifies data into categories without any natural order.

Examples:

* Gender
* Blood group
* Nationality
* Religion

Only classification is meaningful.

---

## 2. Ordinal Scale

The ordinal scale classifies data into ordered categories.

Examples:

* Education level
* Customer satisfaction
* Class ranking
* T-shirt size

The order is meaningful, but the differences between categories are not necessarily equal.

---

## 3. Interval Scale

The interval scale has equal intervals between values but **does not have a true zero**.

Examples:

* Temperature in Celsius
* Temperature in Fahrenheit
* Calendar years

Addition and subtraction are meaningful, but ratios are not.

---

## 4. Ratio Scale

The ratio scale has all the properties of the interval scale and includes a **true zero**, allowing meaningful ratio comparisons.

Examples:

* Height
* Weight
* Age
* Income
* Distance
* Time

All arithmetic operations are meaningful.

---

# Summary Table

| Classification    | Types                             |
| ----------------- | --------------------------------- |
| By Nature         | Qualitative, Quantitative         |
| Quantitative Data | Discrete, Continuous              |
| Measurement Scale | Nominal, Ordinal, Interval, Ratio |

---

# Why Data Types Matter

Identifying the correct data type helps us choose:

* appropriate statistical methods,
* suitable visualizations,
* valid mathematical operations,
* appropriate machine learning algorithms.

For example:

* Numerical data can be summarized using the mean and standard deviation.
* Categorical data is typically summarized using counts and percentages.
* Continuous data is often visualized with histograms.
* Categorical data is commonly displayed using bar charts.

---

# Python Representation

In Python, different data types are commonly represented as:

| Statistical Data | Python Representation                     |
| ---------------- | ----------------------------------------- |
| Categorical data | Strings (`str`)                           |
| Numerical data   | `int`, `float`                            |
| Dataset          | `list`, `NumPy array`, `Pandas DataFrame` |

Python libraries such as **NumPy** and **Pandas** provide efficient tools for storing, manipulating, and analyzing these different types of data.

---

# Summary

* Data can be classified by its nature or by its measurement scale.
* Qualitative data describes categories, while quantitative data represents numerical values.
* Quantitative data is divided into discrete and continuous data.
* Measurement scales include nominal, ordinal, interval, and ratio.
* Understanding data types is essential for selecting appropriate statistical methods and data analysis techniques.
