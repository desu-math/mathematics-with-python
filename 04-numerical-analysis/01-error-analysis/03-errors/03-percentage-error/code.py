# Program to calculate percentage error

true_value = float(input("Enter the true value: "))
approximate_value = float(input("Enter the approximate value: "))

if true_value == 0:
    print("Percentage error is undefined because the true value is zero.")
else:
    absolute_error = abs(true_value - approximate_value)
    relative_error = absolute_error / abs(true_value)
    percentage_error = relative_error * 100

    print("\nStep-by-Step Solution")
    print("---------------------")
    print(f"True Value        = {true_value}")
    print(f"Approximate Value = {approximate_value}")
    print()
    print(f"Absolute Error    = |{true_value} - {approximate_value}|")
    print(f"                  = {absolute_error:.6f}")
    print()
    print(f"Relative Error    = {absolute_error:.6f} / {abs(true_value):.6f}")
    print(f"                  = {relative_error:.6f}")
    print()
    print(f"Percentage Error  = {relative_error:.6f} × 100")
    print(f"                  = {percentage_error:.4f}%")
