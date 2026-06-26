# Program to calculate absolute error

true_value = float(input("Enter the true value: "))
approximate_value = float(input("Enter the approximate value: "))

absolute_error = abs(true_value - approximate_value)

print("\nResult")
print("------")
print(f"True Value        : {true_value}")
print(f"Approximate Value : {approximate_value}")
print(f"Absolute Error    : {absolute_error}")
