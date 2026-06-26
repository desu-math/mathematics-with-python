def count_decimal_places(number):
    number = number.strip()

    # Remove + or - sign
    if number.startswith(("+", "-")):
        number = number[1:]

    # Reject scientific notation
    if "e" in number.lower():
        return None

    # Check for decimal point
    if "." in number:
        decimal_part = number.split(".")[1]
        return len(decimal_part)

    return 0


number = input("Enter a number: ")

decimal_places = count_decimal_places(number)

if decimal_places is None:
    print("Scientific notation is not supported.")
else:
    print(f"\n{number} has {decimal_places} decimal place(s).")
