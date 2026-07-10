# Algorithm: Gaussian Elimination

## Algorithm: Solving a System of Linear Equations Using Gaussian Elimination

**Input:** An augmented matrix representing a system of linear equations.

**Output:** The solution of the system (if it exists).

---

## Step 1: Construct the Augmented Matrix

Write the system of linear equations as an augmented matrix.

Example:

```text
2x + 3y = 7

4x - y = 5
```

becomes

```text
[2   3 | 7
 4  -1 | 5]
```

---

## Step 2: Select the First Pivot

Choose the first nonzero element in the first column as the pivot.

If the pivot is zero:

* Exchange the current row with a lower row containing a nonzero element in the same column.
* If no such row exists, move to the next column.

---

## Step 3: Eliminate the Entries Below the Pivot

For every row below the pivot row:

1. Compute the elimination factor:

```text
factor = (Current Row Pivot Element) / (Pivot Element)
```

2. Update the row using the elementary row operation:

```text
Current Row = Current Row − (factor × Pivot Row)
```

This makes the entry below the pivot equal to zero.

---

## Step 4: Move to the Next Pivot

Move one row down and one column to the right.

Repeat **Step 2** and **Step 3** until all possible pivots have been processed.

The matrix is now in **Row Echelon Form (REF)**.

---

## Step 5: Perform Back Substitution

Start with the last equation.

1. Solve the last unknown.

2. Substitute its value into the equation above.

3. Continue upward until all unknowns have been determined.

---

## Step 6: Display the Solution

Output the values of all unknown variables.

---

# Flow Summary

```text
Start
  │
  ▼
Input System of Equations
  │
  ▼
Convert to Augmented Matrix
  │
  ▼
Select Pivot
  │
  ▼
Is Pivot Equal to Zero?
  │
  ├── Yes → Swap Rows (if possible)
  │
  ▼
Eliminate Entries Below Pivot
  │
  ▼
Move to Next Pivot
  │
  ▼
Repeat Until REF is Obtained
  │
  ▼
Perform Back Substitution
  │
  ▼
Display Solution
  │
  ▼
End
```

---

# Computational Formula

During elimination, each row is updated using:

```text
Rᵢ ← Rᵢ − factor × Rₚ
```

where:

* `Rᵢ` is the current row.
* `Rₚ` is the pivot row.
* `factor = A[i][pivot_column] / A[pivot_row][pivot_column]`.

---

# Important Notes

* Only **elementary row operations** are used.
* The algorithm does **not** change the solution of the system.
* If an entire row becomes:

```text
[0  0  ...  0 | c]
```

where `c ≠ 0`, the system is **inconsistent** and has **no solution**.

* If one or more variables do not receive pivot positions, the system has **infinitely many solutions**.

* If every variable has a pivot position, the system has a **unique solution**.

---

# Time Complexity

For an `n × n` system, Gaussian elimination requires approximately

```text
O(n³)
```

operations.

Although computationally expensive for very large systems, it is one of the most fundamental algorithms in numerical linear algebra and forms the basis of many advanced numerical methods.
