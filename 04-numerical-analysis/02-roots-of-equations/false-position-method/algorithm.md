# Algorithm: False Position (Regula Falsi) Method

## Input

* A continuous function, `f(x)`
* Left endpoint of the interval, `a`
* Right endpoint of the interval, `b`
* Tolerance (acceptable error), `ε`
* Maximum number of iterations, `N`

## Output

* Approximate root of the equation `f(x) = 0`

---

## Algorithm

**Step 1**

Read the function `f(x)`.

**Step 2**

Read the interval endpoints `a` and `b`.

**Step 3**

Read the tolerance `ε` and the maximum number of iterations `N`.

**Step 4**

Evaluate `f(a)` and `f(b)`.

**Step 5**

Check whether

```text
f(a) × f(b) < 0
```

* If the condition is **false**, display

```text
"The False Position Method cannot be applied because the interval does not bracket a root."
```

and stop the algorithm.

* Otherwise, continue to the next step.

---

**Step 6**

Repeat the following steps until either the desired accuracy is achieved or the maximum number of iterations is reached.

1. Compute the next approximation using the False Position formula.

```text
c = (a × f(b) − b × f(a)) / (f(b) − f(a))
```

2. Evaluate

```text
f(c)
```

3. If

```text
f(c) = 0
```

then `c` is the exact root. Display the result and stop.

4. If

```text
f(a) × f(c) < 0
```

then update the interval by setting

```text
b = c
```

Otherwise, update the interval by setting

```text
a = c
```

5. Compute the current interval width.

```text
|b − a|
```

6. If

```text
|b − a| < ε
```

or

```text
|f(c)| < ε
```

stop the iteration.

---

**Step 7**

Display

* The approximate root, `c`
* The function value, `f(c)`
* The number of iterations performed

**End**
