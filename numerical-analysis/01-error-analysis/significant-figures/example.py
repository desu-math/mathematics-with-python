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


"""# Algorithm: Counting Significant Figures

**Input:** A number entered by the user.

**Output:** The number of significant figures.

### Step 1

Read the number as a **string**.

### Step 2

Remove any leading **'+'** or **'-'** sign.

### Step 3

Check whether the number is written in **scientific notation** (contains `e` or `E`).

* If yes, separate the coefficient from the exponent.
* Continue the algorithm using only the coefficient.

### Step 4

Determine whether the number contains a decimal point.

#### Case A: The number contains a decimal point

1. Remove the decimal point.
2. Remove all leading zeros.
3. Count the remaining digits.
4. The count is the number of significant figures.

#### Case B: The number does not contain a decimal point

1. Remove all leading zeros.
2. Remove all trailing zeros.
3. Count the remaining digits.
4. The count is the number of significant figures.

### Step 5

Display the number of significant figures.

### End
"""
