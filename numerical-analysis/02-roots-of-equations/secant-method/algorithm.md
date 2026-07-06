# Algorithm: Secant Method

## Input

* A function, `f(x)`
* First initial approximation, `x₀`
* Second initial approximation, `x₁`
* Tolerance (acceptable error), `ε`
* Maximum number of iterations, `N`

## Output

* Approximate root of the equation `f(x) = 0`

---

## Algorithm

**Step 1**

Read the function `f(x)`.

**Step 2**

Read the first and second initial approximations, `x₀` and `x₁`.

**Step 3**

Read the tolerance `ε` and the maximum number of iterations `N`.

**Step 4**

Evaluate

```text
f(x₀)

f(x₁)
```

---

**Step 5**

Repeat the following steps until either the desired accuracy is achieved or the maximum number of iterations is reached.

### 5.1 Compute the next approximation

Use the Secant Method formula.

```text
x₂ = x₁ − f(x₁)(x₁ − x₀) / (f(x₁) − f(x₀))
```

---

### 5.2 Evaluate

```text
f(x₂)
```

---

### 5.3 Check the stopping criteria

If

```text
|f(x₂)| < ε
```

or

```text
|x₂ − x₁| < ε
```

then stop the iteration.

---

### 5.4 Update the approximations

Replace the previous approximations as follows.

```text
x₀ = x₁

x₁ = x₂
```

Then evaluate

```text
f(x₀)

f(x₁)
```

for the next iteration.

---

**Step 6**

Display

* The approximate root
* The function value at the approximate root
* The number of iterations performed

**End**
