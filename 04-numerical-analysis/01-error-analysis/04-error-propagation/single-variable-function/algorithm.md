# Algorithm: Error Propagation in a Function of a Single Variable

## Input

* A differentiable function, `f(x)`
* The value of the independent variable, `x`
* The error in the independent variable, `Δx`

## Output

* The derivative of the function, `f'(x)`
* The estimated propagated error, `Δy`

---

## Algorithm

**Step 1**

Read the function `f(x)`.

**Step 2**

Read the value of the independent variable, `x`.

**Step 3**

Read the error in the independent variable, `Δx`.

**Step 4**

Compute the derivative of the function:

```text
f'(x)
```

**Step 5**

Evaluate the derivative at the given value of `x`.

**Step 6**

Compute the estimated propagated error using

```text
Δy ≈ f'(x) × Δx
```

**Step 7**

Display:

* The function, `f(x)`
* The derivative, `f'(x)`
* The value of the derivative at the given point
* The estimated propagated error, `Δy`

**End**
