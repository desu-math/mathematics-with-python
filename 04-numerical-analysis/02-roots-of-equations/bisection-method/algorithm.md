# Algorithm: Bisection Method

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
"The Bisection Method cannot be applied because the interval does not bracket a root."
```

and stop the algorithm.

* Otherwise, continue to the next step.

**Step 6**

Repeat the following steps until either the desired accuracy is achieved or the maximum number of iterations is reached.

1. Compute the midpoint

```text
c = (a + b) / 2
```

2. Evaluate `f(c)`.

3. If

```text
f(c) = 0
```

then `c` is the exact root. Display the result and stop.

4. If

```text
f(a) × f(c) < 0
```

then set

```text
b = c
```

Otherwise, set

```text
a = c
```

5. Compute the current interval width

```text
|b − a|
```

6. If

```text
|b − a| < ε
```

then stop the iteration.

**Step 7**

Compute the final approximation

```text
Root = (a + b) / 2
```

**Step 8**

Display

* The approximate root
* The function value at the approximate root
* The number of iterations performed

**End**
