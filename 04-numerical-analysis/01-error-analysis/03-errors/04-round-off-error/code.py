from decimal import Decimal, ROUND_HALF_UP

exact_value = Decimal(input("Enter the exact value: "))
decimal_places = int(input("Round to how many decimal places? "))

pattern = Decimal("1." + "0" * decimal_places)

rounded_value = exact_value.quantize(pattern, rounding=ROUND_HALF_UP)

round_off_error = abs(exact_value - rounded_value)

print("\nStep-by-Step Solution")
print("---------------------")
print(f"Exact Value     = {exact_value}")
print(f"Decimal Places  = {decimal_places}")
print()
print(f"Rounded Value   = {rounded_value}")
print()
print(f"Round-off Error = |{exact_value} - {rounded_value}|")
print(f"                = {round_off_error}")
