```python
"""
Secant Method
-------------
This program finds an approximate root of a nonlinear equation
using the Secant Method.

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
x0 = float(input("Enter the first initial approximation (x0): "))
x1 = float(input("Enter the second initial approximation (x1): "))
tolerance = float(input("Enter the tolerance: "))
max_iterations = int(input("Enter the maximum number of iterations: "))

# Convert the input string into a SymPy expression
f = sympify(function)

# Function evaluator
def evaluate(value):
    return float(f.subs(x, value))

# Evaluate the initial approximations
fx0 = evaluate(x0)
fx1 = evaluate(x1)

# Table header
print("\nIter |       x0 |       x1 |       x2 |     f(x2)")
print("-" * 56)

iteration = 0

while iteration < max_iterations:

    # Check for division by zero
    if fx1 == fx0:
        print("\nError!")
        print("Division by zero encountered.")
        print("f(x1) and f(x0) are equal.")
        break

    # Secant Method formula
    x2 = x1 - fx1 * (x1 - x0) / (fx1 - fx0)

    # Evaluate the function at x2
    fx2 = evaluate(x2)

    # Display the current iteration
    print(f"{iteration + 1:4d} | {x0:8.6f} | {x1:8.6f} | {x2:8.6f} | {fx2:10.6f}")

    # Stopping criteria
    if abs(fx2) < tolerance or abs(x2 - x1) < tolerance:
        break

    # Update the approximations
    x0 = x1
    fx0 = fx1

    x1 = x2
    fx1 = fx2

    iteration += 1

# ---------------------------------
# Output
# ---------------------------------

print("\nApproximate Root :", x2)
print("Function Value   :", fx2)
print("Iterations       :", iteration + 1)
```
