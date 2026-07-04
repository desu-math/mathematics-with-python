# Error Propagation in a Function of a Single Variable

## Introduction

Many mathematical models depend on only one independent variable. If this variable contains a small measurement or approximation error, then the computed value of the function will also contain an error.

Suppose

```text
y = f(x)
```

where the input value `x` has an error `Δx`.

Our objective is to estimate the corresponding error `Δy` in the output.

This process is called **error propagation in a function of a single variable**.

---

# Derivation of the Error Propagation Formula

Suppose the true value of the independent variable is

```text
x
```

but because of measurement or approximation errors, the value used in the computation becomes

```text
x + Δx
```

Therefore, the output changes from

```text
f(x)
```

to

```text
f(x + Δx)
```

Hence, the exact change (or propagated error) in the function is

```text
Δy = f(x + Δx) − f(x)
```

This equation is exact, but it is often difficult to evaluate directly.

To obtain a simpler expression, we use the **first-order Taylor series approximation**.

f(x+\Delta x)\approx f(x)+f'(x)\Delta x

Substituting this approximation into the expression for `Δy` gives

```text
Δy ≈ [f(x) + f'(x) × Δx] − f(x)
```

Simplifying,

```text
Δy ≈ f'(x) × Δx
```

Therefore, the error propagation formula for a function of a single variable is

```text
Estimated Propagated Error = f'(x) × Δx
```

or simply,

```text
Δy ≈ f'(x) × Δx
```

---

# Interpretation of the Formula

The formula

```text
Δy ≈ f'(x) × Δx
```

shows that the propagated error depends on two quantities:

* `Δx` — the error in the input.
* `f'(x)` — the derivative (or sensitivity) of the function.

The derivative tells us how sensitive the function is to changes in its input.

* If `|f'(x)|` is large, a small input error produces a relatively large output error.
* If `|f'(x)|` is small, the output is less sensitive to the input error.
* If `f'(x) = 0`, the propagated error is approximately zero for very small input errors.

---

# Assumptions

The approximation

```text
Δy ≈ f'(x) × Δx
```

is valid when:

* the function is differentiable,
* the input error `Δx` is small,
* higher-order Taylor series terms are neglected.

---

# Applications

Error propagation in a function of a single variable is widely used in:

* Numerical Analysis
* Engineering
* Physics
* Chemistry
* Statistics
* Data Science
* Scientific Computing

It provides a simple and effective way to estimate how uncertainties in the input affect the computed output.

---

# Summary

For a differentiable function

```text
y = f(x)
```

a small error in the input produces an approximate error in the output given by

```text
Δy ≈ f'(x) × Δx
```

This formula is obtained from the first-order Taylor series approximation and is one of the fundamental tools used in numerical analysis for estimating propagated errors.
