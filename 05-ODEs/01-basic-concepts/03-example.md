# Worked Examples: Basic Concepts and Definitions

## Introduction

This document contains worked examples on the fundamental concepts of ordinary differential equations (ODEs).

The examples cover:

1. Identifying ordinary and partial differential equations.
2. Determining the order and degree of differential equations.
3. Classifying differential equations as linear or nonlinear.
4. Identifying homogeneous and nonhomogeneous linear equations.
5. Verifying solutions of differential equations.
6. Finding general and particular solutions.
7. Solving simple initial value problems (IVPs).

Each example includes a step-by-step explanation.

---

## Example 1: Identifying the Type of Differential Equation

### Problem

Determine whether each equation is an ordinary differential equation (ODE) or a partial differential equation (PDE).

**a)** `dy/dx = x + y`

**b)** `∂u/∂t = ∂²u/∂x²`

### Solution

**Part (a)**

`dy/dx = x + y`

The equation contains an ordinary derivative of y with respect to x.

There is one independent variable, x.

Therefore, the equation is an **ODE**.

**Part (b)**

`∂u/∂t = ∂²u/∂x²`

The equation contains partial derivatives of u with respect to t and x.

The function u depends on two independent variables.

Therefore, the equation is a **PDE**.

### Final Answers

* (a) ODE
* (b) PDE

---

## Example 2: Determining the Order and Degree

### Problem

Determine the order and degree of the following differential equations, where the degree is defined.

**a)** `dy/dx + 3y = 0`

**b)** `(dy/dx)^4 + y = 0`

**c)** `d²y/dx² + 5(dy/dx) + 6y = 0`

**d)** `(d³y/dx³)^2 + d²y/dx² + y = 0`

### Solution

**Part (a)**

`dy/dx + 3y = 0`

The highest derivative is dy/dx, which is the first derivative.

Therefore:

* Order = 1
* Degree = 1

**Part (b)**

`(dy/dx)^4 + y = 0`

The highest derivative is dy/dx.

Its exponent is 4.

Therefore:

* Order = 1
* Degree = 4

**Part (c)**

`d²y/dx² + 5(dy/dx) + 6y = 0`

The highest derivative is d²y/dx², which is the second derivative.

Its exponent is 1.

Therefore:

* Order = 2
* Degree = 1

**Part (d)**

`(d³y/dx³)^2 + d²y/dx² + y = 0`

The highest derivative is d³y/dx³, which is the third derivative.

Its exponent is 2.

Therefore:

* Order = 3
* Degree = 2

### Final Answers

| Equation | Order | Degree |
| -------- | ----: | -----: |
| (a)      |     1 |      1 |
| (b)      |     1 |      4 |
| (c)      |     2 |      1 |
| (d)      |     3 |      2 |

### Key Lesson

The order is determined by the highest derivative, while the degree is determined by the exponent of that derivative when the equation is polynomial in its derivatives.

---

## Example 3: Identifying an Undefined Degree

### Problem

Determine the order and degree of:

`sin(dy/dx) + y = 0`

### Solution

**Step 1: Determine the order.**

The equation contains the first derivative dy/dx.

Therefore:

Order = 1.

**Step 2: Examine the degree.**

The derivative appears inside the sine function.

The equation is not polynomial in its derivatives.

Therefore, the degree is undefined under the standard elementary definition.

### Final Answer

* Order = 1
* Degree = Undefined

### Key Lesson

An equation can have a clearly defined order even when its degree is undefined.

---

## Example 4: Classifying Linear and Nonlinear Equations

### Problem

Classify each equation as linear or nonlinear.

**a)** `dy/dx + 4y = x`

**b)** `dy/dx + y² = 0`

**c)** `dy/dx + xy = x²`

**d)** `y(dy/dx) = x`

### Solution

**Part (a)**

`dy/dx + 4y = x`

The equation can be written as:

`dy/dx + P(x)y = Q(x)`

Here, P(x) = 4 and Q(x) = x.

The unknown function and its derivative appear only to the first power.

Therefore, the equation is **linear**.

**Part (b)**

`dy/dx + y² = 0`

The equation contains y².

It cannot be written in the required linear form.

Therefore, the equation is **nonlinear**.

**Part (c)**

`dy/dx + xy = x²`

The coefficient of y is x, which depends only on the independent variable.

The equation is in the standard linear form.

Therefore, the equation is **linear**.

**Part (d)**

`y(dy/dx) = x`

The unknown function y is multiplied by its derivative.

Therefore, the equation is **nonlinear**.

### Final Answers

| Equation | Classification |
| -------- | -------------- |
| (a)      | Linear         |
| (b)      | Nonlinear      |
| (c)      | Linear         |
| (d)      | Nonlinear      |

### Key Lesson

The presence of x multiplied by y does not make an equation nonlinear. However, terms such as y² and y(dy/dx) make the equation nonlinear.

---

## Example 5: Classifying Homogeneous and Nonhomogeneous Linear Equations

### Problem

Classify each equation as homogeneous or nonhomogeneous.

**a)** `dy/dx + 3y = 0`

**b)** `dy/dx + 3y = x`

**c)** `dy/dx + xy = e^x`

### Solution

For a first-order linear ODE, use the standard form:

`dy/dx + P(x)y = Q(x)`

The equation is homogeneous when Q(x) = 0 and nonhomogeneous when Q(x) is not identically zero.

**Part (a)**

`dy/dx + 3y = 0`

The right-hand side is zero.

Therefore, the equation is **homogeneous**.

**Part (b)**

`dy/dx + 3y = x`

The right-hand side is x, which is not identically zero.

Therefore, the equation is **nonhomogeneous**.

**Part (c)**

`dy/dx + xy = e^x`

The right-hand side is e^x, which is not identically zero.

Therefore, the equation is **nonhomogeneous**.

### Final Answers

| Equation | Classification |
| -------- | -------------- |
| (a)      | Homogeneous    |
| (b)      | Nonhomogeneous |
| (c)      | Nonhomogeneous |

All three equations are linear.

---

## Example 6: Verifying a Solution

### Problem

Verify that:

`y = x² + 4`

is a solution of:

`dy/dx = 2x`

### Solution

**Step 1: Identify the proposed solution.**

`y = x² + 4`

**Step 2: Differentiate it.**

Differentiating with respect to x gives:

`dy/dx = 2x`

**Step 3: Compare with the original equation.**

The original equation is:

`dy/dx = 2x`

The derivative of the proposed function satisfies the equation.

Therefore, the proposed function is a solution.

### Final Answer

`y = x² + 4` is a solution of `dy/dx = 2x`.

### Key Lesson

To verify a solution, differentiate the proposed function and substitute it into the original differential equation.

---

## Example 7: Finding the General Solution

### Problem

Find the general solution of:

`dy/dx = 6x²`

### Solution

**Step 1: Write the equation.**

`dy/dx = 6x²`

**Step 2: Integrate both sides with respect to x.**

`y = ∫6x² dx`

**Step 3: Evaluate the integral.**

Using the power rule of integration:

`∫x^n dx = x^(n+1)/(n+1) + C`, for n ≠ -1.

Therefore:

`y = 6(x³/3) + C`

Simplifying:

`y = 2x³ + C`

### Final Answer

`y = 2x³ + C`

This is the general solution.

### Key Lesson

When finding a general solution by indefinite integration, include the arbitrary constant C.

---

## Example 8: Finding a Particular Solution

### Problem

Find the particular solution of:

`dy/dx = 6x²`

given that:

`y(1) = 5`

### Solution

**Step 1: Find the general solution.**

Integrating:

`y = 2x³ + C`

**Step 2: Apply the initial condition.**

The condition is:

`y(1) = 5`

Substitute x = 1 and y = 5:

`5 = 2(1³) + C`

Therefore:

`5 = 2 + C`

**Step 3: Solve for C.**

`C = 3`

**Step 4: Write the particular solution.**

Substitute C = 3 into the general solution.

`y = 2x³ + 3`

### Verification

Differentiate:

`dy/dx = 6x²`

This satisfies the differential equation.

Check the initial condition:

`y(1) = 2(1³) + 3 = 5`

Both conditions are satisfied.

### Final Answer

`y = 2x³ + 3`

---

## Example 9: Understanding a Family of Solution Curves

### Problem

Consider the family of functions:

`y = x² + C`

**a)** Verify that every member of this family satisfies `dy/dx = 2x`.

**b)** Find the member that passes through the point (0, 4).

### Solution

**Part (a): Verification**

Start with:

`y = x² + C`

Differentiate:

`dy/dx = 2x`

The constant C disappears during differentiation.

Therefore, every function in this family satisfies:

`dy/dx = 2x`

**Part (b): Finding the required curve**

The curve passes through (0, 4).

This means:

* x = 0
* y = 4

Substitute these values into:

`y = x² + C`

We obtain:

`4 = 0² + C`

Therefore:

`C = 4`

The required solution is:

`y = x² + 4`

### Final Answer

The solution curve passing through (0, 4) is:

`y = x² + 4`

### Key Lesson

A general solution may represent infinitely many solution curves. An initial condition selects a particular member of the family.

---

## Example 10: Solving an Initial Value Problem

### Problem

Solve the following IVP:

`dy/dx = 3x²`

with the initial condition:

`y(2) = 10`

### Solution

**Step 1: Integrate the differential equation.**

`y = ∫3x² dx`

Therefore:

`y = x³ + C`

**Step 2: Apply the initial condition.**

The condition is:

`y(2) = 10`

Substitute x = 2 and y = 10:

`10 = 2³ + C`

`10 = 8 + C`

Therefore:

`C = 2`

**Step 3: Write the particular solution.**

`y = x³ + 2`

**Step 4: Verify the differential equation.**

Differentiate:

`dy/dx = 3x²`

The differential equation is satisfied.

**Step 5: Verify the initial condition.**

`y(2) = 2³ + 2 = 10`

The initial condition is also satisfied.

### Final Answer

`y = x³ + 2`

---

## Example 11: Determining Whether a Function Solves an IVP

### Problem

Determine whether `y = x² + 1` solves the following IVP:

`dy/dx = 2x`

`y(0) = 2`

### Solution

**Step 1: Check the differential equation.**

Given:

`y = x² + 1`

Differentiate:

`dy/dx = 2x`

The differential equation is satisfied.

**Step 2: Check the initial condition.**

The initial condition requires:

`y(0) = 2`

Substitute x = 0 into the proposed solution:

`y(0) = 0² + 1`

`y(0) = 1`

However, the required value is 2.

Therefore, the initial condition is not satisfied.

### Final Answer

`y = x² + 1` satisfies the differential equation but **does not solve the given IVP**.

### Key Lesson

A function must satisfy both the differential equation and the initial condition to solve an IVP.

---

## Example 12: A More Complete Initial Value Problem

### Problem

Solve the IVP:

`dy/dx = 2x + 1`

with:

`y(0) = 4`

### Solution

**Step 1: Integrate the differential equation.**

`y = ∫(2x + 1) dx`

Therefore:

`y = x² + x + C`

**Step 2: Apply the initial condition.**

Given:

`y(0) = 4`

Substitute x = 0 and y = 4:

`4 = 0² + 0 + C`

Therefore:

`C = 4`

**Step 3: Write the particular solution.**

`y = x² + x + 4`

**Step 4: Verify the differential equation.**

Differentiate:

`dy/dx = 2x + 1`

The original differential equation is satisfied.

**Step 5: Verify the initial condition.**

`y(0) = 0² + 0 + 4 = 4`

The initial condition is satisfied.

### Final Answer

`y = x² + x + 4`

---

## 2. Independent Practice Problems

Try to solve these problems without looking at the worked examples.

### Problem 1: Order and Degree

Determine the order and degree of:

`(d²y/dx²)^3 + 4(dy/dx) + y = 0`

### Problem 2: Classification

Determine whether the following equation is linear or nonlinear:

`dy/dx + 5xy = x²`

### Problem 3: Classification

Determine whether the following equation is linear or nonlinear:

`dy/dx + y³ = x`

### Problem 4: General Solution

Find the general solution of:

`dy/dx = 8x³`

### Problem 5: Particular Solution

Solve:

`dy/dx = 8x³`

given:

`y(1) = 6`

### Problem 6: Verification

Determine whether `y = x³ + 2` solves:

`dy/dx = 3x²`

### Problem 7: Initial Value Problem

Solve:

`dy/dx = 4x + 2`

given:

`y(0) = 3`

### Problem 8: Solution Curves

For the family:

`y = x² + C`

find the particular solution passing through (-1, 5).

### Problem 9: Conceptual Understanding

Explain why a general solution can represent many solution curves.

### Problem 10: Conceptual Understanding

Can a function satisfy a differential equation but fail to solve a given IVP? Explain using an example.

---

## 3. Answers to Independent Practice Problems

Check these answers after attempting the problems.

| Problem | Answer                                                                                         |
| ------- | ---------------------------------------------------------------------------------------------- |
| 1       | Order = 2, Degree = 3                                                                          |
| 2       | Linear                                                                                         |
| 3       | Nonlinear                                                                                      |
| 4       | y = 2x⁴ + C                                                                                    |
| 5       | y = 2x⁴ + 4                                                                                    |
| 6       | Yes, because differentiating gives dy/dx = 3x²                                                 |
| 7       | y = 2x² + 2x + 3                                                                               |
| 8       | y = x² + 4                                                                                     |
| 9       | The arbitrary constant can take different values, producing different solution curves.         |
| 10      | Yes. For example, y = x² + 1 satisfies dy/dx = 2x but does not satisfy the condition y(0) = 2. |

---

## 4. Final Summary

These worked examples demonstrate how to:

* Identify ODEs and PDEs.
* Determine the order and degree of differential equations.
* Classify equations as linear or nonlinear.
* Distinguish homogeneous and nonhomogeneous linear equations.
* Verify proposed solutions.
* Find general and particular solutions.
* Interpret families of solution curves.
* Solve simple initial value problems.

The most important habit is to understand why each step works rather than memorize the final answers.

In later lessons, these foundations will help us understand more advanced methods for solving first-order differential equations.
