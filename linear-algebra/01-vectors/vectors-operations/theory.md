# Vector Operations

## Introduction

Vector operations are mathematical procedures used to combine or manipulate vectors. These operations are fundamental in Linear Algebra and have applications in physics, engineering, computer graphics, robotics, and Data Science.

---

# 1. Vector Addition

Two vectors are added by adding their corresponding components.

For two vectors

```text
u = (u₁, u₂)

v = (v₁, v₂)
```

their sum is

```text
u + v = (u₁ + v₁, u₂ + v₂)
```

### Example

```text
u = (2, 3)

v = (4, 1)

u + v = (6, 4)
```

---

# 2. Vector Subtraction

Vector subtraction is performed by subtracting the corresponding components.

For two vectors

```text
u = (u₁, u₂)

v = (v₁, v₂)
```

their difference is

```text
u − v = (u₁ − v₁, u₂ − v₂)
```

### Example

```text
u = (5, 7)

v = (2, 3)

u − v = (3, 4)
```

---

# 3. Scalar Multiplication

Scalar multiplication multiplies every component of a vector by the same scalar.

For a scalar **k** and a vector

```text
v = (x, y)
```

the product is

```text
k v = (k x, k y)
```

### Example

```text
k = 3

v = (2, 4)

3v = (6, 12)
```

---

# 4. Dot Product (Scalar Product)

The **dot product** of two vectors is a scalar.

For two vectors

```text
u = (u₁, u₂)

v = (v₁, v₂)
```

the dot product is

```text
u · v = u₁v₁ + u₂v₂
```

In three dimensions,

```text
u · v = u₁v₁ + u₂v₂ + u₃v₃
```

The dot product can also be expressed as

```text
u · v = |u||v| cos θ
```

where **θ** is the angle between the vectors.

### Example

```text
u = (2, 3)

v = (4, 5)

u · v = (2)(4) + (3)(5)

      = 8 + 15

      = 23
```

---

# 5. Cross Product (Vector Product)

The **cross product** is defined only for three-dimensional vectors.

For

```text
u = (u₁, u₂, u₃)

v = (v₁, v₂, v₃)
```

the cross product is

```text
u × v =

(u₂v₃ − u₃v₂,
 u₃v₁ − u₁v₃,
 u₁v₂ − u₂v₁)
```

Its magnitude is

```text
|u × v| = |u||v| sin θ
```

The resulting vector is perpendicular to both **u** and **v**.

### Example

```text
u = (1, 0, 0)

v = (0, 1, 0)

u × v = (0, 0, 1)
```

---

# 6. Projection of One Vector onto Another

The projection of a vector **u** onto a vector **v** is the component of **u** in the direction of **v**.

It is given by

```text
projᵥ(u) = (u · v / |v|²) v
```

### Example

If

```text
u = (3, 4)

v = (1, 0)
```

then

```text
projᵥ(u) = (3, 0)
```

---

# 7. Angle Between Two Vectors

The angle between two vectors is determined using the dot product.

For vectors **u** and **v**,

```text
cos θ = (u · v) / (|u||v|)
```

Therefore,

```text
θ = cos⁻¹[(u · v) / (|u||v|)]
```

### Example

For

```text
u = (1, 0)

v = (0, 1)
```

```text
u · v = 0
```

Hence,

```text
θ = 90°
```

showing that the vectors are perpendicular.

---

# Applications

Vector operations are widely used in:

* Solving systems of equations
* Computer graphics and animation
* Robotics and navigation
* Physics and engineering
* Data Science and Machine Learning

---

# Summary

* **Vector addition** combines two vectors by adding corresponding components.
* **Vector subtraction** finds the difference between two vectors.
* **Scalar multiplication** changes the magnitude of a vector.
* The **dot product** measures similarity and is used to compute angles.
* The **cross product** produces a vector perpendicular to two 3D vectors.
* **Projection** finds the component of one vector along another.
* The **angle between vectors** is computed using the dot product.
