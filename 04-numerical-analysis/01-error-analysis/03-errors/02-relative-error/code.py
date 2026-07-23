# Program to calculate relative error

true_value = float(input("Enter the true value: "))
approximate_value = float(input("Enter the approximate value: "))

if true_value == 0:
    print("Relative error is undefined because the true value is zero.")
else:
    absolute_error = abs(true_value - approximate_value)
    relative_error = absolute_error / abs(true_value)

    print("\nResult")
    print("------")
    print(f"True Value        : {true_value}")
    print(f"Approximate Value : {approximate_value}")
    print(f"Absolute Error    : {absolute_error}")
    print(f"Relative Error    : {relative_error}")
