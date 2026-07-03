# truncation error for taylor series of f(x) = e^x = 1 + x + x^2/2! + x^3/3! + x^4/4! + ...
import math

# Input
x = float(input("Enter x: "))
n = int(input("Enter the number of Taylor series terms: "))

# Taylor series approximation
approximation = 0

for k in range(n):
    approximation += (x ** k) / math.factorial(k)

# Exact value
exact = math.exp(x)

# Truncation error
truncation_error = abs(exact - approximation)

# Output
print("\nResult")
print("------")
print(f"Exact value         = {exact}")
print(f"Approximate value   = {approximation}")
print(f"Truncation error    = {truncation_error}")
