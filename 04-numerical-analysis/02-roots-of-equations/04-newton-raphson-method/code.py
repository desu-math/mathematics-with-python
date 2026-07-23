```python
"""
Newton-Raphson Method
---------------------
This program finds an approximate root of a nonlinear equation
using the Newton-Raphson Method.

Author: Desalu Horsa
Repository: mathematics-with-python
"""

from sympy import symbols, sympify, diff

# Define the symbolic variable
x = symbols('x')

# ---------------------------------
# Input
# ---------------------------------

function = input("Enter f(x): ")
x0 = float(input("Enter the initial approximation (x0): "))
tolerance = float(input("Enter the tolerance: "))
max_iterations = int(input("Enter the maximum number of iterations: "))

# Convert the input string into a SymPy expression
f = sympify(function)

# Compute the derivative automatically
df = diff(f, x)

# Function evaluator
def evaluate(expression, value):
    return float(expression.subs(x, value))

# Display the derivative
print("\nDerivative:")
print(f"f'(x) = {df}")

# Table header
print("\nIter |       x0 |       x1 |     f(x1)")
print("-" * 48)

iteration = 0

while iteration < max_iterations:

    # Evaluate the function and its derivative
    fx0 = evaluate(f, x0)
    dfx0 = evaluate(df, x0)

    # Check for division by zero
    if dfx0 == 0:
        print("\nError!")
        print("The derivative is zero.")
        print("The Newton-Raphson Method cannot continue.")
        break

    # Newton-Raphson formula
    x1 = x0 - fx0 / dfx0

    # Evaluate the function at x1
    fx1 = evaluate(f, x1)

    # Display the current iteration
    print(f"{iteration + 1:4d} | {x0:8.6f} | {x1:8.6f} | {fx1:10.6f}")

    # Stopping criteria
    if abs(fx1) < tolerance or abs(x1 - x0) < tolerance:
        break

    # Update the approximation
    x0 = x1

    iteration += 1

# ---------------------------------
# Output
# ---------------------------------

print("\nApproximate Root :", x1)
print("Function Value   :", fx1)
print("Iterations       :", iteration + 1)
```
