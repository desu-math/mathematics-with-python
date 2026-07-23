# Algorithm: Gauss-Jordan Elimination

## Algorithm: Solving a System of Linear Equations Using Gauss-Jordan Elimination

**Input:** An augmented matrix representing a system of linear equations.

**Output:** The solution of the system (if it exists).

---

# Step 1: Construct the Augmented Matrix

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

# Step 2: Select the First Pivot

Choose the first nonzero element in the current column as the pivot.

If the pivot is zero:

* Swap the current row with a lower row containing a nonzero element in the same column.
* If no such row exists, move to the next column.

---

# Step 3: Normalize the Pivot Row

Divide every element of the pivot row by the pivot value.

```text
Pivot Row = Pivot Row ÷ Pivot
```

After this operation, the pivot becomes **1**.

---

# Step 4: Eliminate All Other Entries in the Pivot Column

For every row except the pivot row:

1. Compute the elimination factor:

```text
factor = Current Row Pivot Element
```

2. Update the row:

```text
Current Row = Current Row − (factor × Pivot Row)
```

This makes every other entry in the pivot column equal to **0**.

---

# Step 5: Move to the Next Pivot

Move one row down and one column to the right.

Repeat **Step 2** through **Step 4** until every pivot has been processed.

The matrix is now in **Reduced Row Echelon Form (RREF)**.

---

# Step 6: Read the Solution

Since the matrix is in RREF, the solution is obtained directly from the last column.

No back substitution is required.

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
Is Pivot Zero?
  │
  ├── Yes → Swap Rows (if possible)
  │
  ▼
Normalize Pivot Row
  │
  ▼
Eliminate All Other Entries
in the Pivot Column
  │
  ▼
Move to Next Pivot
  │
  ▼
Repeat Until RREF is Obtained
  │
  ▼
Read Solution Directly
  │
  ▼
End
```

---

# Computational Formula

### Pivot Normalization

```text
Rₚ ← Rₚ ÷ Pivot
```

where:

* `Rₚ` is the pivot row.
* `Pivot` is the pivot element.

---

### Elimination

For every row except the pivot row:

```text
Rᵢ ← Rᵢ − factor × Rₚ
```

where:

```text
factor = A[i][pivot_column]
```

Unlike Gaussian Elimination, elimination is performed **both below and above** the pivot.

---

# Important Notes

* Every pivot must become **1**.
* Every pivot column must contain only one nonzero element (the pivot itself).
* The final matrix is in **Reduced Row Echelon Form (RREF)**.
* The solution can be read directly from the last column.
* If a row becomes:

```text
[0  0  ...  0 | c]
```

where `c ≠ 0`, the system is **inconsistent** and has **no solution**.

* If one or more variables do not receive pivot positions, the system has **infinitely many solutions**.

* If every variable has a pivot position, the system has a **unique solution**.

---

# Time Complexity

For an `n × n` system, Gauss-Jordan Elimination requires approximately

```text
O(n³)
```

operations.

Although it has the same asymptotic time complexity as Gaussian Elimination, it generally performs **more row operations**, making it slightly slower in practice.
