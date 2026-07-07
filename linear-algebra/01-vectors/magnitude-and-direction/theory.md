# Magnitude and Direction

## Introduction

A vector is completely described by two properties:

* **Magnitude** – the size or length of the vector.
* **Direction** – the orientation of the vector in space.

Both properties are needed to distinguish one vector from another.

---

# Magnitude of a Vector

The **magnitude** (or **norm**) of a vector is its length.

The magnitude of a vector **v** is denoted by

```text
|v|
```

or

```text
||v||
```

For a two-dimensional vector

```text
v = (x, y)
```

the magnitude is

```text
|v| = √(x² + y²)
```

For a three-dimensional vector

```text
v = (x, y, z)
```

the magnitude is

```text
|v| = √(x² + y² + z²)
```

### Example

If

```text
v = (3, 4)
```

then

```text
|v| = √(3² + 4²)
     = √25
     = 5
```

---

# Direction of a Vector

The **direction** of a vector indicates where the vector points.

In two dimensions, the direction is usually measured as the angle **θ** between the vector and the positive x-axis.

For a vector

```text
v = (x, y)
```

the direction angle is

```text
θ = tan⁻¹(y/x)
```

In practice, Python's `atan2(y, x)` function is preferred because it correctly determines the angle in all four quadrants.

### Example

For

```text
v = (3, 4)
```

```text
θ = tan⁻¹(4/3)

θ ≈ 53.13°
```

---

# Important Notes

* The magnitude of a vector is always **non-negative**.
* A vector with magnitude **0** is called the **zero vector**.
* Two vectors may have the same magnitude but different directions.
* Two vectors may have the same direction but different magnitudes.

---

# Applications

Magnitude and direction are used in:

* Physics (force, velocity, acceleration)
* Engineering
* Navigation
* Computer Graphics
* Robotics
* Data Science (measuring vector length and similarity)

---

# Summary

* **Magnitude** measures the length of a vector.
* **Direction** specifies the orientation of a vector.
* The magnitude is computed using the distance formula.
* In two dimensions, the direction is commonly expressed as the angle with the positive x-axis.
* Together, magnitude and direction completely describe a vector.
