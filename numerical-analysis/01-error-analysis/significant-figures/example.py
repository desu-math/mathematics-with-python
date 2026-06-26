def count_significant_figures(number):
    num = number.strip()

    # Remove sign
    if num.startswith(('+', '-')):
        num = num[1:]

    # Scientific notation
    if 'e' in num.lower():
        coefficient = num.lower().split('e')[0]
        return count_significant_figures(coefficient)

    # Decimal number
    if '.' in num:
        # Remove decimal point
        digits = num.replace('.', '')

        # Remove leading zeros
        digits = digits.lstrip('0')

        return len(digits)

    # Whole number
    else:
        # Remove leading zeros
        digits = num.lstrip('0')

        # Remove trailing zeros (ambiguous)
        digits = digits.rstrip('0')

        return len(digits)


number = input("Enter a number: ")

count = count_significant_figures(number)

print(f"\n{number} has {count} significant figure(s).")

