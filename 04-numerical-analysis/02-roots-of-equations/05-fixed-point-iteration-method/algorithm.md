# Algorithm: Fixed-Point Iteration Method

## Input

* A nonlinear equation, `f(x) = 0`
* An initial approximation, `x₀`
* Tolerance (acceptable error), `ε`
* Maximum number of iterations, `N`

## Output

* Approximate root of the equation

---

## Algorithm

### Step 1

Read the equation

```text
f(x) = 0
```

---

### Step 2

Rearrange the equation into an equivalent fixed-point form

```text
x = g(x)
```

Choose a function `g(x)` that is expected to converge.

If possible, verify that

```text
|g′(x)| < 1
```

near the expected root.

---

### Step 3

Read the initial approximation `x₀`.

---

### Step 4

Read the tolerance `ε` and the maximum number of iterations `N`.

---

### Step 5

Repeat the following steps until either the desired accuracy is achieved or the maximum number of iterations is reached.

#### 5.1 Compute the next approximation

```text
x₁ = g(x₀)
```

#### 5.2 Compute the approximate error

```text
Error = |x₁ − x₀|
```

#### 5.3 Check the stopping criterion

If

```text
Error < ε
```

then stop the iteration.

#### 5.4 Update the approximation

```text
x₀ = x₁
```

Repeat Step 5.

---

### Step 6

Display

* Approximate root
* Approximate error
* Number of iterations

**End**
