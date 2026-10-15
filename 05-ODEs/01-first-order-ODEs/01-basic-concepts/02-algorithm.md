# Algorithms: Basic Concepts and Definitions

## 1. Purpose

This document provides step-by-step procedures for identifying and classifying differential equations, determining their order and degree, and verifying their solutions.

These procedures establish the foundation for solving differential equations in later topics.

---

## Algorithm 1: Identifying the Type of Differential Equation

### Objective

Determine whether a differential equation is an ordinary differential equation (ODE) or a partial differential equation (PDE).

### Procedure

1. Examine the derivatives appearing in the equation.
2. If the equation contains ordinary derivatives with respect to one independent variable, classify it as an ODE.
3. If the equation contains partial derivatives of a function depending on two or more independent variables, classify it as a PDE.
4. Record the classification.

### Example

Given:

`dy/dx + y = x`

The equation contains an ordinary derivative with respect to x.

**Result: ODE**

Given:

`∂u/∂t = ∂²u/∂x²`

The equation contains partial derivatives of a function depending on x and t.

**Result: PDE**

---

## Algorithm 2: Determining the Order of a Differential Equation

### Objective

Find the order of a differential equation.

### Procedure

1. List the derivatives appearing in the equation.
2. Identify the derivative with the highest order.
3. Determine the order of that derivative.
4. Report that value as the order of the differential equation.

### Example

Given:

`d³y/dx³ + 5(d²y/dx²) + 2(dy/dx) + y = 0`

The derivatives are:

* First derivative: dy/dx
* Second derivative: d²y/dx²
* Third derivative: d³y/dx³

The highest derivative is the third derivative.

**Result: Order = 3**

### Important Rule

Do not determine the order by looking at the exponent of a derivative. The order depends only on the highest derivative appearing in the equation.

---

## Algorithm 3: Determining the Degree of a Differential Equation

### Objective

Find the degree of a differential equation when the degree is defined.

### Procedure

1. Identify the highest-order derivative.
2. Check whether the equation is polynomial in its derivatives.
3. If necessary, simplify the equation algebraically to remove radicals or fractional powers of derivatives, while checking that the transformations are valid.
4. Identify the exponent of the highest-order derivative.
5. Report that exponent as the degree.
6. If the equation cannot be expressed as a polynomial in its derivatives under the standard definition, report that the degree is undefined.

### Example 1

Given:

`(d²y/dx²)^3 + dy/dx + y = 0`

The highest derivative is d²y/dx².

Its exponent is 3.

**Result: Order = 2, Degree = 3**

### Example 2

Given:

`sin(dy/dx) + y = 0`

The derivative appears inside a trigonometric function.

The equation is not polynomial in its derivatives.

**Result: Order = 1, Degree = Undefined under the standard definition**

### Important Rule

The degree is not necessarily the exponent of the highest derivative as the equation is first written. The equation must be expressed appropriately as a polynomial in its derivatives.

---

## Algorithm 4: Classifying a First-Order ODE as Linear or Nonlinear

### Objective

Determine whether a first-order ODE is linear or nonlinear.

### Standard Linear Form

`dy/dx + P(x)y = Q(x)`

Here, P(x) and Q(x) depend only on x.

### Procedure

1. Identify the unknown function y and its first derivative dy/dx.

2. Try to express the equation in the standard form:

   `dy/dx + P(x)y = Q(x)`

3. Check whether y and dy/dx appear only to the first power.

4. Check that y is not multiplied by its derivative.

5. Check that the equation does not contain nonlinear functions of y, such as y², sin(y), or e^y.

6. If the equation can be written in the standard linear form, classify it as linear.

7. Otherwise, classify it as nonlinear.

### Example 1

Given:

`dy/dx + xy = x²`

Compare it with:

`dy/dx + P(x)y = Q(x)`

Here:

* P(x) = x
* Q(x) = x²

Both depend only on x.

**Result: Linear**

### Example 2

Given:

`dy/dx + y² = 0`

The equation contains y².

It cannot be written in the required linear form.

**Result: Nonlinear**

### Important Rule

The presence of xy does not make an equation nonlinear. The variable x acts as a coefficient of y.

However, y² or y(dy/dx) makes the equation nonlinear.

---

## Algorithm 5: Classifying a Linear First-Order ODE as Homogeneous or Nonhomogeneous

### Objective

Determine whether a linear first-order ODE is homogeneous or nonhomogeneous.

### Standard Form

`dy/dx + P(x)y = Q(x)`

### Procedure

1. First, confirm that the equation is linear.
2. Rewrite it in the standard form if necessary.
3. Examine the right-hand side, Q(x).
4. If Q(x) = 0, classify the equation as homogeneous.
5. If Q(x) is not identically zero, classify the equation as nonhomogeneous.

### Example 1

Given:

`dy/dx + 4y = 0`

The right-hand side is zero.

**Result: Linear and homogeneous**

### Example 2

Given:

`dy/dx + 4y = x²`

The right-hand side is x², which is not identically zero.

**Result: Linear and nonhomogeneous**

### Important Rule

This classification refers to the standard form of a linear differential equation. The word "homogeneous" can have other meanings in other areas of differential equations.

---

## Algorithm 6: Verifying a Proposed Solution

### Objective

Determine whether a proposed function satisfies a differential equation.

### Procedure

1. Write down the original differential equation.
2. Identify the proposed solution.
3. Differentiate the proposed solution as many times as required.
4. Substitute the function and its derivatives into the original equation.
5. Simplify both sides.
6. If the equation is satisfied throughout the required domain, the function is a solution on that domain.
7. If an initial condition is given, substitute the initial values and check that the condition is also satisfied.

### Example

Verify whether:

`y = x² + 3`

satisfies:

`dy/dx = 2x`

**Step 1: Differentiate the proposed solution.**

Given:

`y = x² + 3`

Differentiate:

`dy/dx = 2x`

**Step 2: Compare with the original equation.**

The original equation is:

`dy/dx = 2x`

The derivative matches the right-hand side.

**Result: The proposed function is a solution.**

### Example with an Initial Condition

Suppose the IVP is:

`dy/dx = 2x`

`y(0) = 3`

The proposed solution is:

`y = x² + 3`

We have already verified that it satisfies the differential equation.

Now check the initial condition:

`y(0) = 0² + 3 = 3`

The initial condition is satisfied.

**Result: The proposed function solves the IVP.**

---

## Algorithm 7: Finding a Particular Solution from an Initial Condition

### Objective

Determine the arbitrary constant in a general solution using an initial condition.

### Procedure

1. Obtain the general solution of the differential equation.
2. Identify the arbitrary constant.
3. Substitute the initial values into the general solution.
4. Solve the resulting equation for the constant.
5. Substitute the constant into the general solution.
6. Verify the differential equation and initial condition.

### Example

Solve:

`dy/dx = 2x`

given:

`y(1) = 5`

**Step 1: Find the general solution.**

Integrate:

`y = x² + C`

**Step 2: Apply the initial condition.**

Substitute x = 1 and y = 5:

`5 = 1² + C`

**Step 3: Solve for the constant.**

`5 = 1 + C`

`C = 4`

**Step 4: Write the particular solution.**

`y = x² + 4`

**Step 5: Verify.**

Differentiate:

`dy/dx = 2x`

Check the initial condition:

`y(1) = 1² + 4 = 5`

Both conditions are satisfied.

**Final answer: y = x² + 4**

---

## 2. General Problem-Solving Checklist

When examining a differential equation, use the following checklist:

1. Identify whether the equation is an ODE or a PDE.
2. Determine the order.
3. Determine the degree, if defined.
4. Classify the equation as linear or nonlinear when applicable.
5. If it is a linear first-order equation, determine whether it is homogeneous or nonhomogeneous.
6. If a solution is provided, verify it by differentiation and substitution.
7. If an initial condition is provided, check whether the proposed solution satisfies it.
8. Present the final result clearly.

**Note:** These steps are for identifying, classifying, and verifying differential equations. They are not a universal algorithm for solving every differential equation. Different equations require different solution methods.
