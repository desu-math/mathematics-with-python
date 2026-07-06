```python
"""
False Position (Regula Falsi) Method
------------------------------------
This program finds an approximate root of a continuous function
using the False Position Method.

Author: Desalu Horsa
Repository: mathematics-with-python
"""

from sympy import symbols, sympify

# Define the symbolic variable
x = symbols('x')

# ---------------------------------
# Input
# ---------------------------------

function = input("Enter f(x): ")
a = float(input("Enter the left endpoint (a): "))
b = float(input("Enter the right endpoint (b): "))
tolerance = float(input("Enter the tolerance: "))
max_iterations = int(input("Enter the maximum number of iterations: "))

# Convert the input string into a SymPy expression
f = sympify(function)

# Function evaluator
def evaluate(value):
    return float(f.subs(x, value))

# Evaluate the endpoints
fa = evaluate(a)
fb = evaluate(b)

# Check whether the interval brackets a root
if fa * fb >= 0:
    print("\nError!")
    print("The interval does not satisfy")
    print("f(a) × f(b) < 0")
    print("Choose another interval.")
    exit()

# Table header
print("\nIter |        a |        b |        c |      f(c)")
print("-" * 56)

iteration = 0

while iteration < max_iterations:

    # False Position formula
    c = (a * fb - b * fa) / (fb - fa)

    # Evaluate the function at c
    fc = evaluate(c)

    # Display current iteration
    print(f"{iteration + 1:4d} | {a:8.6f} | {b:8.6f} | {c:8.6f} | {fc:10.6f}")

    # Stopping criteria
    if abs(fc) < tolerance or abs(b - a) < tolerance:
        break

    # Update the interval
    if fa * fc < 0:
        b = c
        fb = fc
    else:
        a = c
        fa = fc

    iteration += 1

# ---------------------------------
# Output
# ---------------------------------

print("\nApproximate Root :", c)
print("Function Value   :", fc)
print("Iterations       :", iteration + 1)
```
