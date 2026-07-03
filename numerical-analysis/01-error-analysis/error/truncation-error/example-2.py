#Truncation error of Taylor series expansion of f(x) = sin(x) = x - x^3/3! + x^5/5! - x^7/7! + x^9/9! - ... = sum k=0 to k=n-1{(-1)^k* x^(2k+1) / (2k+1)!}
import math

# Input
x = float(input("Enter x (in radians): "))
n = int(input("Enter the number of Taylor series terms: "))

# Taylor series approximation
approximation = 0

for k in range(n):
    term = ((-1) ** k) * (x ** (2 * k + 1)) / math.factorial(2 * k + 1)
    approximation += term

# Exact value
exact = math.sin(x)

# Truncation error
truncation_error = abs(exact - approximation)

# Output
print("\nResult")
print("------")
print(f"Exact value         = {exact}")
print(f"Approximate value   = {approximation}")
print(f"Truncation error    = {truncation_error}")
