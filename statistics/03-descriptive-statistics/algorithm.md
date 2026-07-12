# Algorithms for Descriptive Statistics

Descriptive statistics consists of several statistical measures used to summarize and describe a dataset. Each measure has its own computation procedure.

---

# Algorithm 1: Computing the Mean

**Input:** A dataset containing `n` numerical observations.

**Output:** The arithmetic mean of the dataset.

### Steps

1. Read the dataset.
2. Compute the sum of all observations.
3. Count the number of observations.
4. Divide the sum by the number of observations.
5. Display the mean.

---

# Algorithm 2: Computing the Median

**Input:** A dataset containing `n` numerical observations.

**Output:** The median of the dataset.

### Steps

1. Read the dataset.
2. Sort the observations in ascending order.
3. Count the number of observations.
4. If the number of observations is odd:

   * Select the middle value.
5. Otherwise:

   * Compute the average of the two middle values.
6. Display the median.

---

# Algorithm 3: Computing the Mode

**Input:** A dataset containing `n` observations.

**Output:** The mode(s) of the dataset.

### Steps

1. Read the dataset.
2. Count the frequency of each unique value.
3. Find the largest frequency.
4. Identify the value(s) having that frequency.
5. Display the mode(s).

---

# Algorithm 4: Computing the Range

**Input:** A dataset containing `n` numerical observations.

**Output:** The range of the dataset.

### Steps

1. Read the dataset.
2. Find the largest value.
3. Find the smallest value.
4. Subtract the smallest value from the largest value.
5. Display the range.

---

# Algorithm 5: Computing the Variance

**Input:** A dataset containing `n` numerical observations.

**Output:** The variance of the dataset.

### Steps

1. Read the dataset.
2. Compute the mean.
3. Subtract the mean from each observation.
4. Square each deviation.
5. Compute the average of the squared deviations.
6. Display the variance.

---

# Algorithm 6: Computing the Standard Deviation

**Input:** A dataset containing `n` numerical observations.

**Output:** The standard deviation of the dataset.

### Steps

1. Read the dataset.
2. Compute the variance.
3. Compute the square root of the variance.
4. Display the standard deviation.

---

# Algorithm 7: Computing the Interquartile Range (IQR)

**Input:** A dataset containing `n` numerical observations.

**Output:** The interquartile range.

### Steps

1. Read the dataset.
2. Sort the observations in ascending order.
3. Determine the first quartile (Q1).
4. Determine the third quartile (Q3).
5. Compute:

```text id="dgol1u"
IQR = Q3 − Q1
```

6. Display the interquartile range.

---

# Summary

| Measure                   | Purpose                                 |
| ------------------------- | --------------------------------------- |
| Mean                      | Average value                           |
| Median                    | Middle value                            |
| Mode                      | Most frequent value                     |
| Range                     | Total spread                            |
| Variance                  | Average squared deviation from the mean |
| Standard Deviation        | Spread measured in the original units   |
| Interquartile Range (IQR) | Spread of the middle 50% of the data    |
