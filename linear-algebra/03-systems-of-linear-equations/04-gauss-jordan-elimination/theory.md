# Gauss-Jordan Elimination

## Introduction

**Gauss-Jordan Elimination** is an extension of the Gaussian Elimination method used to solve systems of linear equations.

Like Gaussian Elimination, it transforms the augmented matrix using **elementary row operations**. However, instead of stopping at **Row Echelon Form (REF)**, it continues until the matrix reaches **Reduced Row Echelon Form (RREF)**.

The final matrix allows the solution to be read directly without using back substitution.

---

# Main Idea

The Gauss-Jordan elimination process is:

```text
Original System

        ↓

Augmented Matrix

        ↓

Row Echelon Form (REF)

        ↓

Reduced Row Echelon Form (RREF)

        ↓

Read the Solution Directly
```

Unlike Gaussian Elimination, no back substitution is required.

---

# Relationship with Gaussian Elimination

Both methods begin in the same way.

### Gaussian Elimination

* Converts the matrix to **Row Echelon Form (REF)**.
* Uses **back substitution** to obtain the solution.

### Gauss-Jordan Elimination

* Converts the matrix to **Reduced Row Echelon Form (RREF)**.
* Reads the solution directly from the final matrix.

Therefore, Gauss-Jordan Elimination can be viewed as:

```text
Gaussian Elimination

        +

Additional Elimination Above Each Pivot
```

---

# Row Echelon Form (REF)

A matrix is in Row Echelon Form if:

1. All nonzero rows are above zero rows.
2. Each pivot is to the right of the pivot in the row above.
3. All entries below each pivot are zero.

Example:

```text
[1   2 | 5
 0   3 | 6]
```

This matrix is in REF.

---

# Reduced Row Echelon Form (RREF)

A matrix is in Reduced Row Echelon Form if:

1. It satisfies all conditions of REF.
2. Every pivot is equal to **1**.
3. Every pivot is the only nonzero element in its column.

Example:

```text
[1   0 | 1
 0   1 | 2]
```

This matrix is in RREF.

The solution can be read immediately:

```text
x = 1

y = 2
```

---

# Elementary Row Operations

Gauss-Jordan Elimination uses the same three elementary row operations as Gaussian Elimination.

## 1. Row Switching

Exchange two rows.

Notation:

```text
Rᵢ ↔ Rⱼ
```

---

## 2. Row Multiplication

Multiply a row by a nonzero constant.

Notation:

```text
Rᵢ → kRᵢ
```

where:

```text
k ≠ 0
```

This operation is commonly used to make each pivot equal to **1**.

---

## 3. Row Addition

Add a multiple of one row to another.

Notation:

```text
Rᵢ → Rᵢ + kRⱼ
```

This operation is used to eliminate entries both **below** and **above** each pivot.

---

# Example

Consider the system:

```text
x + y = 5

2x + 3y = 12
```

The augmented matrix is:

```text
[1   1 | 5
 2   3 |12]
```

---

## Step 1: Eliminate Below the First Pivot

Apply:

```text
R₂ → R₂ − 2R₁
```

Result:

```text
[1   1 |5
 0   1 |2]
```

The matrix is now in **Row Echelon Form**.

---

## Step 2: Eliminate Above the Second Pivot

Apply:

```text
R₁ → R₁ − R₂
```

Result:

```text
[1   0 |3
 0   1 |2]
```

The matrix is now in **Reduced Row Echelon Form**.

The solution is:

```text
x = 3

y = 2
```

No back substitution is needed.

---

# REF vs RREF

| Row Echelon Form (REF)           | Reduced Row Echelon Form (RREF)      |
| -------------------------------- | ------------------------------------ |
| Zeros below pivots               | Zeros above and below pivots         |
| Pivot may be any nonzero value   | Pivot is always 1                    |
| Requires back substitution       | No back substitution                 |
| Produced by Gaussian Elimination | Produced by Gauss-Jordan Elimination |

---

# Advantages

* Solution is obtained directly.
* No back substitution is required.
* Produces the Reduced Row Echelon Form.
* Useful for solving multiple systems and finding matrix inverses.

---

# Disadvantages

* Requires more row operations than Gaussian Elimination.
* Slightly slower for large systems.
* In practice, many numerical computing libraries prefer Gaussian Elimination or LU decomposition for efficiency.

---

# Applications

Gauss-Jordan Elimination is used in:

* Solving systems of linear equations.
* Finding the inverse of a matrix.
* Determining the rank of a matrix.
* Solving engineering and scientific problems.
* Computer algebra systems.

---

# Python Implementation Concept

The implementation begins exactly like Gaussian Elimination:

1. Construct the augmented matrix.
2. Perform forward elimination to obtain REF.

Then it continues with two additional steps:

* Divide each pivot row so the pivot becomes **1**.
* Eliminate all entries above each pivot.

The final matrix is in Reduced Row Echelon Form, and the solution can be read directly from the last column.

---

# Summary

* Gauss-Jordan Elimination is an extension of Gaussian Elimination.
* It transforms an augmented matrix into Reduced Row Echelon Form (RREF).
* Every pivot becomes **1**, and all other entries in the pivot column become **0**.
* Unlike Gaussian Elimination, it does not require back substitution.
* It is widely used for solving linear systems, finding matrix inverses, and determining matrix rank.
