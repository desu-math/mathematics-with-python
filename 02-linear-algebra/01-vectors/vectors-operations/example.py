import math

# ------------------------------------------
# Helper Functions
# ------------------------------------------

def magnitude(v):
    return math.sqrt(sum(component ** 2 for component in v))


def input_vector(dimension):
    vector = []

    print(f"\nEnter the {dimension} components:")

    for i in range(dimension):
        value = float(input(f"Component {i + 1}: "))
        vector.append(value)

    return vector


# ------------------------------------------
# Vector Operations
# ------------------------------------------

def addition():
    dimension = int(input("Dimension (2 or 3): "))

    u = input_vector(dimension)
    v = input_vector(dimension)

    result = [u[i] + v[i] for i in range(dimension)]

    print("\nResult =", result)


def subtraction():
    dimension = int(input("Dimension (2 or 3): "))

    u = input_vector(dimension)
    v = input_vector(dimension)

    result = [u[i] - v[i] for i in range(dimension)]

    print("\nResult =", result)


def scalar_multiplication():
    dimension = int(input("Dimension (2 or 3): "))

    scalar = float(input("Enter the scalar: "))

    v = input_vector(dimension)

    result = [scalar * value for value in v]

    print("\nResult =", result)


def dot_product():
    dimension = int(input("Dimension (2 or 3): "))

    u = input_vector(dimension)
    v = input_vector(dimension)

    result = sum(u[i] * v[i] for i in range(dimension))

    print("\nDot Product =", result)


def cross_product():

    print("\nCross product is defined only for 3D vectors.")

    u = input_vector(3)
    v = input_vector(3)

    result = [
        u[1] * v[2] - u[2] * v[1],
        u[2] * v[0] - u[0] * v[2],
        u[0] * v[1] - u[1] * v[0]
    ]

    print("\nCross Product =", result)


def projection():

    dimension = int(input("Dimension (2 or 3): "))

    u = input_vector(dimension)
    v = input_vector(dimension)

    dot = sum(u[i] * v[i] for i in range(dimension))
    mag_squared = magnitude(v) ** 2

    if mag_squared == 0:
        print("\nProjection onto the zero vector is undefined.")
        return

    factor = dot / mag_squared

    result = [factor * value for value in v]

    print("\nProjection =", result)


def angle():

    dimension = int(input("Dimension (2 or 3): "))

    u = input_vector(dimension)
    v = input_vector(dimension)

    dot = sum(u[i] * v[i] for i in range(dimension))

    mag_u = magnitude(u)
    mag_v = magnitude(v)

    if mag_u == 0 or mag_v == 0:
        print("\nAngle with the zero vector is undefined.")
        return

    cos_theta = dot / (mag_u * mag_v)

    # Avoid numerical rounding errors
    cos_theta = max(-1, min(1, cos_theta))

    theta = math.degrees(math.acos(cos_theta))

    print(f"\nAngle = {theta:.2f}°")


# ------------------------------------------
# Main Program
# ------------------------------------------

while True:

    print("\n========== Vector Operations ==========")
    print("1. Vector Addition")
    print("2. Vector Subtraction")
    print("3. Scalar Multiplication")
    print("4. Dot Product")
    print("5. Cross Product")
    print("6. Projection")
    print("7. Angle Between Two Vectors")
    print("8. Exit")

    choice = input("\nEnter your choice: ")

    if choice == "1":
        addition()

    elif choice == "2":
        subtraction()

    elif choice == "3":
        scalar_multiplication()

    elif choice == "4":
        dot_product()

    elif choice == "5":
        cross_product()

    elif choice == "6":
        projection()

    elif choice == "7":
        angle()

    elif choice == "8":
        print("\nThank you for using the Vector Operations Calculator.")
        break

    else:
        print("\nInvalid choice. Please try again.")
