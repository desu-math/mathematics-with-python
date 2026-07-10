# Algorithm: Solving Systems of Linear Equations Using the Matrix Inverse Method

## Algorithm: Solving a Linear System Using the Matrix Inverse

**Input:** A coefficient matrix **A** and a constant vector **B**.

**Output:** The solution vector **X** (if it exists).

---

# Step 1: Construct the Matrix Equation

Write the system of linear equations in the form:

```text
AX = B
```

where:

* **A** is the coefficient matrix.
* **X** is the unknown vector.
* **B** is the constant vector.

---

# Step 2: Verify That the Matrix is Invertible

Compute the determinant of the coefficient matrix.

If

```text
det(A) = 0
```

then:

* The inverse of **A** does not exist.
* Stop the algorithm.

Otherwise, continue to the next step.

---

# Step 3: Compute the Inverse of the Coefficient Matrix

Find the inverse of **A**.

```text
A⁻¹
```

This can be done manually (using the adjoint method) or by using a numerical library.

---

# Step 4: Multiply the Inverse by the Constant Vector

Compute the solution vector using

```text
X = A⁻¹B
```

This multiplication gives the values of all unknown variables.

---

# Step 5: Display the Solution

Print the solution vector.

Each element of **X** corresponds to one unknown variable.

---

# Flow Summary

```text
Start
  │
  ▼
Input Coefficient Matrix (A)
and Constant Vector (B)
  │
  ▼
Compute det(A)
  │
  ▼
Is det(A) = 0?
  │
  ├── Yes → Matrix is not invertible
  │          Stop
  │
  ▼
Compute A⁻¹
  │
  ▼
Multiply

X = A⁻¹B
  │
  ▼
Display Solution
  │
  ▼
End
```

---

# Computational Formula

The Matrix Inverse Method is based on the equation

```text
AX = B
```

Multiplying both sides by the inverse of **A** gives

```text
A⁻¹AX = A⁻¹B
```

Since

```text
A⁻¹A = I
```

the solution becomes

```text
X = A⁻¹B
```

---

# Important Notes

* The coefficient matrix must be **square**.
* The coefficient matrix must be **invertible**.
* The determinant of the coefficient matrix must be **nonzero**.
* If the inverse does not exist, this method cannot be used.
* Every element of the resulting vector **X** represents the value of one unknown variable.

---

# Time Complexity

The overall computational cost is approximately

```text
O(n³)
```

because computing the inverse of an `n × n` matrix requires cubic time, and the matrix multiplication also contributes to the total computation.

For large systems, Gaussian Elimination is generally preferred because it avoids explicitly computing the inverse matrix and is usually more efficient in practice.
