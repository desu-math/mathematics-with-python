
# Algorithm: Counting Significant Figures

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
