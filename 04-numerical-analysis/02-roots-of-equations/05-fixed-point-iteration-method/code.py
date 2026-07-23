```python
"""
Fixed-Point Iteration Method
----------------------------
This program finds an approximate root of a nonlinear equation
using the Fixed-Point Iteration Method.

Author: Desalu Horsa
Repository: mathematics-with-python
"""

from sympy import symbols, sympify

# Define the symbolic variable
x = symbols('x')

# ---------------------------------
# Input
# ---------------------------------

print("Enter g(x) from the equation x = g(x)")
function = input("g(x) = ")

x0 = float(input("Enter the initial approximation (x0): "))
tolerance = float(input("Enter the tolerance: "))
max_iterations = int(input("Enter the maximum number of iterations: "))

# Convert the input into a SymPy expression
g = sympify(function)

# Function evaluator
def evaluate(expression, value):
    return float(expression.subs(x, value))

# ---------------------------------
# Iteration
# ---------------------------------

print("\nIter |       x0 |       x1 |      Error")
print("-" * 46)

iteration = 0

while iteration < max_iterations:

    # Compute the next approximation
    x1 = evaluate(g, x0)

    # Compute the approximate error
    error = abs(x1 - x0)

    # Display the current iteration
    print(f"{iteration + 1:4d} | {x0:8.6f} | {x1:8.6f} | {error:10.6f}")

    # Check the stopping criterion
    if error < tolerance:
        break

    # Update the approximation
    x0 = x1

    iteration += 1

# ---------------------------------
# Output
# ---------------------------------

print("\nApproximate Root :", x1)
print("Approximate Error:", error)
print("Iterations       :", iteration + 1)
```
