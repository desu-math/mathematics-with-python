# Algorithm: Counting Decimal Places

**Input:** A number entered by the user.

**Output:** The number of decimal places.

### Step 1

Read the number as a **string**.

### Step 2

Remove any leading **'+'** or **'-'** sign.

### Step 3

Check whether the number is written in **scientific notation** (contains `e` or `E`).

* If yes, display a message that this program does not support scientific notation.
* Stop the algorithm.

### Step 4

Check whether the number contains a decimal point.

#### Case A: The number contains a decimal point

1. Locate the decimal point.
2. Count every digit to the right of the decimal point.
3. The count is the number of decimal places.

#### Case B: The number does not contain a decimal point

1. The number has **0 decimal places**.

### Step 5

Display the number of decimal places.

### End
