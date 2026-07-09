# Algorithm: Matrix Inverse

## Algorithm 1: Finding the Inverse of a Matrix (Without NumPy)

**Input:** A square matrix **A**

**Output:** The inverse of **A**, if it exists.

### Step 1

Input the order **n** of the square matrix.

### Step 2

Input all elements of matrix **A**.

### Step 3

Check whether the matrix is square.

* If the matrix is not square, stop the algorithm because an inverse is not defined.

### Step 4

Compute the determinant of **A**.

### Step 5

Check the determinant.

* If `det(A) = 0`, display:

```text
The matrix is singular.
Inverse does not exist.
```

Stop the algorithm.

### Step 6

For each element `aᵢⱼ`:

1. Delete row **i** and column **j**.
2. Compute the determinant of the remaining submatrix.
3. Store the result as the minor `Mᵢⱼ`.

Repeat until all minors are computed.

### Step 7

Compute the cofactor of each element using

```text
Cᵢⱼ = (-1)^(i+j) × Mᵢⱼ
```

Store all cofactors to form the **cofactor matrix**.

### Step 8

Transpose the cofactor matrix to obtain the **adjoint (adjugate)** matrix.

### Step 9

Compute the inverse using

```text
A⁻¹ = (1 / det(A)) × adj(A)
```

### Step 10

Display the inverse matrix.

---

# Algorithm 2: Finding the Inverse Using NumPy

**Input:** A square matrix **A**

**Output:** The inverse of **A**, if it exists.

### Step 1

Import the NumPy library.

### Step 2

Input the order **n** of the square matrix.

### Step 3

Input all elements of matrix **A**.

### Step 4

Convert the matrix into a NumPy array.

### Step 5

Compute the determinant using

```text
np.linalg.det(A)
```

### Step 6

Check the determinant.

* If the determinant is approximately zero, display:

```text
The matrix is singular.
Inverse does not exist.
```

Stop the algorithm.

### Step 7

Compute the inverse using

```text
np.linalg.inv(A)
```

### Step 8

Display the inverse matrix.

---

# Flow Summary

```text
Start
  │
  ▼
Input Matrix
  │
  ▼
Is Matrix Square?
  │
  ├── No → Stop
  │
  ▼ Yes
Compute Determinant
  │
  ▼
Is det(A) = 0 ?
  │
  ├── Yes → Matrix is Singular → Stop
  │
  ▼ No
Find Minors
  │
  ▼
Find Cofactors
  │
  ▼
Find Adjoint
  │
  ▼
Compute Inverse
  │
  ▼
Display Result
  │
  ▼
End
```
