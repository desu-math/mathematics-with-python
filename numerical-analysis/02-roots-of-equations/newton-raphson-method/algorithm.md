# Algorithm: Newton–Raphson Method

## Input

* A function, `f(x)`
* The derivative of the function, `f′(x)`
* An initial approximation, `x₀`
* Tolerance (acceptable error), `ε`
* Maximum number of iterations, `N`

## Output

* Approximate root of the equation `f(x) = 0`

---

## Algorithm

**Step 1**

Read the function `f(x)`.

**Step 2**

Read the derivative of the function, `f′(x)`.

**Step 3**

Read the initial approximation, `x₀`.

**Step 4**

Read the tolerance `ε` and the maximum number of iterations `N`.

---

**Step 5**

Repeat the following steps until either the desired accuracy is achieved or the maximum number of iterations is reached.

### 5.1 Evaluate the function and its derivative

Compute

```text
f(x₀)

f′(x₀)
```

---

### 5.2 Check whether the derivative is zero

If

```text
f′(x₀) = 0
```

display

```text
"The derivative is zero. The Newton–Raphson Method cannot continue."
```

and stop the algorithm.

---

### 5.3 Compute the next approximation

Use the Newton–Raphson formula.

```text
x₁ = x₀ − f(x₀) / f′(x₀)
```

---

### 5.4 Evaluate the function at the new approximation

Compute

```text
f(x₁)
```

---

### 5.5 Check the stopping criteria

If

```text
|f(x₁)| < ε
```

or

```text
|x₁ − x₀| < ε
```

then stop the iteration.

---

### 5.6 Update the approximation

Replace

```text
x₀ = x₁
```

Then continue to the next iteration.

---

**Step 6**

Display

* The approximate root
* The function value at the approximate root
* The number of iterations performed

**End**
