# Significant Figures

## Introduction

In mathematics, science, engineering, and numerical analysis, numbers are often obtained by **measuring** or **approximating** a quantity rather than knowing its exact value. Because every measurement has a limited precision, we need a way to indicate how many digits in a number are trustworthy.

**Significant figures** (or **significant digits**) are the digits in a number that carry meaningful information about its precision.
**Precision** refers to the level of detail in a measurement. In other words, it tells **us how closely we know the value of a quantity**.
**Accuracy** refers to how close a measurement is to the true value.

Understanding significant figures is one of the first steps in numerical analysis because computers and measuring instruments cannot represent every real number exactly. The number of significant figures tells us how accurately a value is known.

---

# Why Are Significant Figures Important?

Imagine two students measure the length of the same table.

* Student A records **2 m**.
* Student B records **2.00 m**.

Although both measurements have the same numerical value, they do **not** have the same precision.

* **2 m** means the length is known only to the nearest meter.
* **2.00 m** means the length is known to the nearest hundredth of a meter.

Therefore,

> The number of significant figures tells us not only the value of a number but also the accuracy of that value.

This idea is extremely important in numerical analysis because calculations performed with inaccurate data cannot produce highly accurate results.

---

# Definition

A **significant figure** is any digit that contributes to the precision of a measured or approximated number.

Simply,

> Significant figures are the digits we trust in a numerical value.

For example,

```
25.74
```

All four digits are significant.

Therefore,

```
25.74 has 4 significant figures.
```

---

# Rules for Identifying Significant Figures

There are several simple rules for determining the number of significant figures in a number.

## Rule 1: Every Non-Zero Digit Is Significant

Digits from **1 to 9** are always significant.

### Examples

| Number | Significant Figures |
| ------ | ------------------- |
| 8      | 1                   |
| 37     | 2                   |
| 425    | 3                   |
| 9128   | 4                   |

Explanation:

Every non-zero digit contributes to the precision.

---

## Rule 2: Zeros Between Non-Zero Digits Are Significant

Zeros that appear between non-zero digits are always counted.

### Examples

| Number | Significant Figures |
| ------ | ------------------- |
| 101    | 3                   |
| 2005   | 4                   |
| 30.07  | 4                   |
| 40008  | 5                   |

Example:

```
101
```

Digits:

```
1 0 1
```

The zero lies between two non-zero digits.

Therefore,

```
101 has 3 significant figures.
```

---

## Rule 3: Leading Zeros Are NOT Significant

Leading zeros are zeros that appear before the first non-zero digit.

Their only purpose is to locate the decimal point.

### Examples

| Number  | Significant Figures |
| ------- | ------------------- |
| 0.3     | 1                   |
| 0.05    | 1                   |
| 0.0072  | 2                   |
| 0.00081 | 2                   |

Example

```
0.0072
```

Ignoring the leading zeros leaves

```
72
```

Therefore,

```
0.0072 has 2 significant figures.
```

---

## Rule 4: Trailing Zeros After a Decimal Point Are Significant

Trailing zeros are zeros at the end of a number.

If they come after a decimal point, they indicate increased precision.

### Examples

| Number | Significant Figures |
| ------ | ------------------- |
| 2.0    | 2                   |
| 5.60   | 3                   |
| 12.300 | 5                   |
| 0.4500 | 4                   |

Example

```
5.60
```

The zero shows that the measurement is accurate to the hundredths place.

Therefore,

```
5.60 has 3 significant figures.
```

---

## Rule 5: Trailing Zeros in Whole Numbers Without a Decimal Point May Be Ambiguous

Numbers such as

```
1500
```

can be interpreted in different ways.

Without additional information, it is impossible to know whether the trailing zeros are intended to be significant.

For example,

```
1500
```

could represent

* 2 significant figures
* 3 significant figures
* 4 significant figures

depending on how the number was obtained.

To avoid ambiguity, scientific notation is preferred.

Examples

| Scientific Notation | Significant Figures |
| ------------------- | ------------------- |
| 1.5 × 10³           | 2                   |
| 1.50 × 10³          | 3                   |
| 1.500 × 10³         | 4                   |

Scientific notation clearly indicates the intended precision.

---

# Counting Significant Figures: Worked Examples

## Example 1

```
58.32
```

Digits:

```
5 8 3 2
```

Answer:

**4 significant figures**

---

## Example 2

```
0.00481
```

Ignore the leading zeros.

Remaining digits:

```
481
```

Answer:

**3 significant figures**

---

## Example 3

```
3040
```

* The zero between 3 and 4 is significant.
* The final zero is ambiguous because there is no decimal point.

Common interpretation:

**3 significant figures**

---

## Example 4

```
0.02030
```

Leading zeros are ignored.

Remaining digits:

```
2 0 3 0
```

Answer:

**4 significant figures**

---

# Significant Figures in Scientific Notation

Scientific notation makes identifying significant figures straightforward.

Examples

| Number       | Significant Figures |
| ------------ | ------------------- |
| 3.45 × 10⁶   | 3                   |
| 6.020 × 10²³ | 4                   |
| 1.200 × 10⁻⁴ | 4                   |
| 7 × 10⁵      | 1                   |

Notice that only the coefficient determines the number of significant figures.

The exponent does **not** affect the count.

---

# Common Mistakes

Many beginners make the following mistakes:

❌ Counting leading zeros as significant.

Example:

```
0.00052
```

Correct answer:

**2 significant figures**

---

❌ Ignoring zeros between non-zero digits.

Example:

```
1002
```

Correct answer:

**4 significant figures**

---

❌ Assuming all ending zeros are significant.

Example:

```
2500
```

Without a decimal point or scientific notation, the number of significant figures is uncertain.

---

# Applications of Significant Figures

Significant figures are used in many fields, including:

* Numerical analysis
* Engineering
* Physics
* Chemistry
* Statistics
* Data science
* Computer simulations

They help us:

* represent measured values correctly,
* understand the precision of data,
* reduce unnecessary digits in calculations, and
* communicate numerical results accurately.

---

# Summary

* Significant figures indicate the precision of a measured or approximated value.
* All non-zero digits are significant.
* Zeros between non-zero digits are significant.
* Leading zeros are never significant.
* Trailing zeros after a decimal point are significant.
* Trailing zeros in whole numbers without a decimal point are often ambiguous.
* Scientific notation is the best way to express the intended number of significant figures.

Mastering significant figures is essential before studying rounding errors, truncation errors, and other numerical analysis topics because almost every numerical computation depends on understanding the precision of the numbers involved.
