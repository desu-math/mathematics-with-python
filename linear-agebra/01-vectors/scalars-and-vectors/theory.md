# Scalars, Vectors, and Vector Notation

## Introduction

Before studying vector operations, it is important to understand the basic concepts of **scalars**, **vectors**, and how vectors are represented mathematically.

---

# Scalars

A **scalar** is a quantity that has **magnitude only**. It is completely described by a single numerical value and an appropriate unit.

### Examples

* Mass: 5 kg
* Time: 10 s
* Temperature: 25 °C
* Distance: 12 m
* Energy: 100 J

---

# Vectors

A **vector** is a quantity that has both **magnitude** and **direction**.

To describe a vector completely, we must specify both its size and the direction in which it acts.

### Examples

* Displacement: 8 m east
* Velocity: 20 m/s north
* Force: 50 N downward
* Acceleration: 9.8 m/s² downward

---

# Scalars vs. Vectors

| Scalar                                    | Vector                                 |
| ----------------------------------------- | -------------------------------------- |
| Has magnitude only                        | Has magnitude and direction            |
| Represented by a single number            | Represented by magnitude and direction |
| Ordinary arithmetic is usually sufficient | Vector operations are required         |

---

# Vector Notation

Vectors are represented in several equivalent ways.

### 1. Boldface Letter

Commonly used in printed books.

```text
v
```

(Printed in **bold**, e.g., **v**.)

Example:

```text
v = (3, 4)
```

---

### 2. Letter with an Arrow

Commonly used in handwritten work.

```text
→v
```

Example:

```text
→AB
```

represents the vector from point **A** to point **B**.

---

### 3. Component Form

A vector can be represented by its components.

In two dimensions:

```text
(a, b)
```

or

```text
⟨a, b⟩
```

Example:

```text
(3, 4)
```

means the vector has an x-component of 3 and a y-component of 4.

In three dimensions:

```text
(a, b, c)
```

Example:

```text
(2, -1, 5)
```

---

### 4. Unit Vector Form

A vector may also be written using unit vectors.

In two dimensions:

```text
a i + b j
```

In three dimensions:

```text
a i + b j + c k
```

where:

* **i** is the unit vector along the x-axis.
* **j** is the unit vector along the y-axis.
* **k** is the unit vector along the z-axis.

Example:

```text
3i + 4j
```

is equivalent to

```text
(3, 4)
```

---

# Why Are Vectors Important?

Vectors are used to describe quantities that have direction and are fundamental in many fields, including:

* Mathematics
* Physics
* Engineering
* Computer Graphics
* Robotics
* Data Science
* Machine Learning

In Data Science, each data sample is often represented as a vector, making vectors one of the foundational concepts for many algorithms.

---

# Summary

* A **scalar** has magnitude only.
* A **vector** has both magnitude and direction.
* Vectors can be represented using **boldface letters**, **arrow notation**, **component form**, or **unit vector form**.
* Understanding vectors is essential for studying Linear Algebra and its applications in Data Science.
