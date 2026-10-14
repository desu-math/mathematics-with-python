# Ordinary Differential Equations

**A comprehensive study of Ordinary Differential Equations (ODEs) combining mathematical theory, analytical problem-solving, and Python implementations.**

This repository is a structured learning resource developed to strengthen my understanding of Ordinary Differential Equations as a final-year Applied Mathematics student. It combines theoretical explanations, mathematical derivations, step-by-step solution algorithms, hand-worked examples, and Python implementations to develop both analytical and computational problem-solving skills.


The course follows the subject organization of *Advanced Engineering Mathematics, 10th Edition*, by Erwin Kreyszig, Herbert Kreyszig, and Edward J. Norminton, as its principal reference.

---

## Table of Contents

* [1. Course Objectives](#1-course-objectives)
* [2. Learning Philosophy](#2-learning-philosophy)
* [3. Course Structure](#3-course-structure)
* [4. Organization of Each Topic](#4-organization-of-each-topic)
* [5. Course Syllabus](#5-course-syllabus)
* [6. Mathematical and Computational Approach](#6-mathematical-and-computational-approach)
* [7. Technologies and Tools](#7-technologies-and-tools)
* [8. Learning Outcomes](#8-learning-outcomes)
* [9. Intended Audience](#9-intended-audience)
* [10. How to Use This Repository](#10-how-to-use-this-repository)
* [11. Future Development](#11-future-development)
* [12. Reference](#12-reference)

---

## 1. Course Objectives

The main objective of this repository is to develop a systematic understanding of ordinary differential equations, from fundamental concepts to analytical solution techniques, numerical methods, and applications.

Specifically, this project aims to:

* Establish a strong theoretical foundation in ODEs, including their definitions, classifications, properties, and mathematical interpretations.
* Understand the derivations of important formulas and methods rather than memorizing them without understanding.
* Develop the ability to identify the type of a differential equation and select an appropriate solution method.
* Master analytical techniques for solving first-order, second-order, and higher-order differential equations.
* Understand initial value problems, boundary conditions where relevant, and the existence and uniqueness of solutions.
* Develop proficiency in solving differential equations by hand using clear, systematic procedures.
* Translate mathematical solution techniques into Python implementations.
* Understand the principles behind numerical methods and implement selected algorithms without relying entirely on existing libraries.
* Use scientific Python libraries to solve problems efficiently and verify analytical or manually computed results.
* Apply ODEs to mathematical modeling and real-world problems.
* Develop the ability to interpret, visualize, and evaluate mathematical and computational results.
* Strengthen the theoretical knowledge and problem-solving skills needed for university exit examinations and further academic study.

## 2. Learning Philosophy

This repository emphasizes understanding, mathematical reasoning, and independent problem-solving rather than memorization alone.

Each topic is approached from several complementary perspectives.

### 2.1 Theory Before Application

Important definitions, assumptions, mathematical properties, and derivations are studied before applying a solution technique.

The objective is to understand why a method works, when it can be applied, and what limitations it may have.

### 2.2 Manual Problem-Solving

Worked examples demonstrate how to solve mathematical problems step by step using analytical techniques.

This develops the ability to solve examination problems independently, without depending on computational tools.

### 2.3 Algorithmic Thinking

Mathematical procedures are organized into clear algorithms that describe the sequence of operations required to solve a problem.

This connects mathematical reasoning with the logical structure of computer programs.

### 2.4 Independent Implementation

Where appropriate, solution methods are implemented in Python without relying on specialized numerical or symbolic libraries to perform the main calculation.

These implementations help demonstrate the mathematical principles underlying computational methods.

### 2.5 Library-Based Computation

Selected problems are also solved using established scientific Python libraries.

Comparing independent implementations with library-based solutions helps develop an understanding of computational efficiency, accuracy, and practical software use.

### 2.6 Visualization and Interpretation

Graphs, direction fields, solution curves, and other visual representations are included when they improve conceptual understanding.

Computational results are interpreted mathematically rather than presented as numerical outputs alone.

### 2.7 Verification and Critical Thinking

Solutions are checked whenever possible using substitution, differentiation, initial conditions, independent computational methods, or numerical error analysis.

The goal is to develop the habit of evaluating whether a mathematical result is correct and meaningful.

---

## 3. Course Structure

The repository is organized by mathematical topics. Each topic has its own directory containing the relevant theoretical explanations, solution algorithms, worked examples, and Python implementations where appropriate.

A typical topic follows this structure:

```text
topic-name/
├── theory.md
├── algorithm.md
├── example.md
├── code1.py
└── code2.py
```

Not every topic must contain all five files. The structure is adapted to the mathematical nature of the topic.

For example, some analytical methods may not require a Python implementation, while numerical methods may benefit from both independent and library-based implementations.

### Purpose of Each File

| File           | Purpose                                                                                                  |
| -------------- | -------------------------------------------------------------------------------------------------------- |
| `theory.md`    | Explains definitions, concepts, assumptions, mathematical derivations, properties, and interpretations.  |
| `algorithm.md` | Presents the step-by-step procedure for applying the relevant solution method.                           |
| `example.md`   | Demonstrates complete manual solutions with intermediate calculations and explanations.                  |
| `code1.py`     | Implements the relevant mathematical procedure in Python from the underlying algorithm, where practical. |
| `code2.py`     | Demonstrates a corresponding implementation using suitable scientific Python libraries, where practical. |

This organization separates mathematical understanding, procedural knowledge, manual calculations, and computational implementation while showing how they work together.

---

## 4. Organization of Each Topic

### 4.1 `theory.md`

This file provides the conceptual and theoretical foundation of the topic.

Depending on the subject, it may contain:

* Learning objectives.
* Motivation and applications.
* Prerequisite knowledge.
* Fundamental definitions and terminology.
* Classification of differential equations.
* Mathematical intuition and conceptual explanations.
* Formal mathematical statements.
* Derivations of important formulas and results.
* Assumptions and conditions under which a method applies.
* Important properties and theorems.
* Visual interpretations, diagrams, and graphs where useful.
* Relationships between different solution methods.
* Common misconceptions and mistakes.
* Summary of essential concepts.
* Practice questions.
* References and suggestions for further study.

The emphasis is on explaining both **what a mathematical result means and why it is valid**.

### 4.2 `algorithm.md`

This file translates a mathematical method into an ordered procedure.

Depending on the topic, it may contain:

* The problem to be solved.
* Required inputs and expected outputs.
* Conditions that must be satisfied before applying the method.
* The main mathematical formulas.
* Step-by-step solution procedures.
* Decision rules for selecting an appropriate method.
* Pseudocode where useful.
* Stopping criteria for iterative numerical algorithms.
* Computational limitations and possible sources of error.
* A discussion of computational complexity when relevant.

The algorithms should be sufficiently clear that a reader can follow them manually or translate them into Python.

### 4.3 `example.md`

This file contains manually worked mathematical examples.

Each example aims to demonstrate the reasoning process, not merely the final answer.

A typical worked example includes:

1. The problem statement.
2. Identification and classification of the differential equation.
3. Selection of an appropriate solution method.
4. The mathematical formula or principle being applied.
5. Detailed intermediate calculations.
6. Application of initial or boundary conditions, when applicable.
7. The final solution.
8. Verification of the result where possible.
9. Interpretation of the solution when meaningful.

Examples range from fundamental exercises to more challenging problems that combine multiple concepts.

### 4.4 `code1.py` — Independent Python Implementation

This file contains a Python implementation of the relevant mathematical method without relying on a specialized library to perform the main calculation.

The implementation may include:

* Input handling and validation.
* The mathematical procedure expressed as code.
* Functions for reusable calculations.
* Appropriate comments explaining important steps.
* Error handling where necessary.
* Test cases.
* Comparison with a known analytical result or manually computed example.

For example, a numerical method such as Euler's method can be implemented directly using its mathematical recurrence relation.

The objective is to demonstrate that I understand the algorithm sufficiently well to implement it independently.

### 4.5 `code2.py` — Library-Based Python Implementation

This file demonstrates how the same or a closely related problem can be solved using established scientific Python libraries.

Depending on the topic, suitable tools may include:

* **SymPy** for symbolic mathematics, differentiation, integration, and analytical differential-equation solving.
* **NumPy** for numerical calculations and array operations.
* **SciPy** for numerical integration and solving initial value problems.
* **Matplotlib** for plotting solution curves and visualizing numerical results.

The implementation should explain which library functions are being used, what they calculate, and how their outputs should be interpreted.

Where meaningful, the result is compared with the independent implementation or analytical solution.

The purpose is to understand both the mathematical method and its practical use through established computational tools.

---

## 5. Course Syllabus

The syllabus is organized around the ODE material in *Advanced Engineering Mathematics*, 10th Edition.

### Module 1: First-Order Ordinary Differential Equations

**Primary reference: Chapter 1**

Topics include:

* Basic concepts and definitions.
* Order, degree where defined, and classification of differential equations.
* Solutions of differential equations and solution curves.
* Initial value problems.
* Mathematical modeling using first-order ODEs.
* Geometric interpretation of differential equations.
* Direction fields and Euler's method.
* Separable differential equations.
* Exact differential equations and integrating factors.
* Linear first-order differential equations.
* Bernoulli equations.
* Population dynamics.
* Orthogonal trajectories.
* Existence and uniqueness of solutions.

### Module 2: Second-Order Linear Ordinary Differential Equations

**Primary reference: Chapter 2**

Topics include:

* Homogeneous linear ODEs of second order.
* Fundamental solutions and general solutions.
* Linear independence of solutions.
* Homogeneous equations with constant coefficients.
* Characteristic equations and their roots.
* Modeling free oscillations of mass-spring systems.
* Euler-Cauchy equations.
* Existence and uniqueness of solutions.
* The Wronskian.
* Nonhomogeneous linear ODEs.
* Methods for finding particular solutions.
* Forced oscillations and resonance.
* Mathematical modeling of electric circuits.
* Variation of parameters.

### Module 3: Higher-Order Linear Ordinary Differential Equations

**Primary reference: Chapter 3**

Topics include:

* General theory of homogeneous linear ODEs.
* Fundamental systems of solutions.
* Linear independence and general solutions.
* Homogeneous equations with constant coefficients.
* Characteristic equations and their roots.
* Nonhomogeneous higher-order linear equations.
* Methods for finding particular solutions.
* Initial conditions and the determination of arbitrary constants.

### Module 4: Systems of Ordinary Differential Equations

**Primary reference: Chapter 4**

Topics include:

* Mathematical modeling using systems of ODEs.
* First-order systems and equivalent formulations.
* Basic theory of systems of differential equations.
* Linear systems and fundamental solution matrices.
* The Wronskian for systems.
* Constant-coefficient systems.
* Eigenvalues and eigenvectors in solving linear systems.
* Phase-plane methods.
* Critical points and stability.
* Qualitative analysis of nonlinear systems.
* Nonhomogeneous linear systems.

### Module 5: Series Solutions of Ordinary Differential Equations

**Primary reference: Chapter 5**

Topics include:

* Power series solutions.
* Determination of series coefficients.
* Ordinary points and singular points.
* Legendre's equation.
* Legendre polynomials.
* The Frobenius method.
* Bessel's equation.
* Bessel functions of the first and second kinds.
* Special functions arising from differential equations.

### Module 6: Laplace Transforms and Differential Equations

**Primary reference: Chapter 6**

Topics include:

* Definition of the Laplace transform.
* Linearity and basic transform formulas.
* First shifting theorem.
* Laplace transforms of derivatives and integrals.
* Solving initial value problems using Laplace transforms.
* Unit step and Heaviside functions.
* Second shifting theorem.
* Dirac's delta function and impulse problems.
* Partial fraction decomposition in inverse transforms.
* Convolution theorem.
* Differentiation and integration of transforms.
* Differential equations with variable coefficients, as covered by the text.
* Systems of ODEs using Laplace transforms.

### Module 7: Numerical Methods for Ordinary Differential Equations

**Primary reference: Chapter 21, Sections 21.1–21.3**

This module extends the analytical material by studying computational methods for approximating solutions.

Topics include:

* Numerical solution of initial value problems.
* Euler's method.
* Improved numerical methods for first-order ODEs.
* Error and accuracy in numerical approximations.
* Step-size selection and its effects.
* Multistep methods.
* Numerical methods for systems of ODEs.
* Numerical methods for higher-order ODEs.
* Comparison of numerical approximations with exact solutions where available.
* Implementation and visualization of numerical solutions in Python.

The precise methods covered in this module will follow the selected sections of the reference book and the needs of the course.

---

## 6. Mathematical and Computational Approach

The repository connects four complementary aspects of studying differential equations.

| Aspect                | Main question                                                    | Intended outcome                                              |
| --------------------- | ---------------------------------------------------------------- | ------------------------------------------------------------- |
| Mathematical theory   | Why does the method work?                                        | Conceptual understanding and mathematical reasoning.          |
| Manual computation    | How is the method applied to a problem?                          | Analytical problem-solving ability.                           |
| Algorithm development | What sequence of operations solves the problem?                  | Procedural and algorithmic understanding.                     |
| Python implementation | How can the method be implemented and evaluated computationally? | Programming skills and computational problem-solving ability. |

Where appropriate, topics will also include mathematical modeling, graphical interpretation, numerical experimentation, and verification.

### Analytical and Numerical Solutions

Analytical methods aim to obtain mathematical expressions for solutions. Numerical methods approximate solution values at selected points.

These approaches complement each other.

Analytical solutions help establish exact mathematical behavior when closed-form solutions are available. Numerical solutions help investigate problems when analytical solutions are difficult to obtain or unavailable in a convenient form.

Comparing the two can reveal approximation errors, computational limitations, and the practical strengths of different methods.

### Verification of Results

Whenever practical, solutions will be checked using one or more of the following:

* Substitution into the original differential equation.
* Differentiation of an analytical solution.
* Verification of initial conditions.
* Comparison with a manually calculated example.
* Comparison between independent and library-based implementations.
* Numerical error analysis.
* Graphical comparison of solution curves.

Verification is treated as an essential part of mathematical problem-solving rather than an optional final step.

---

## 7. Technologies and Tools

The project primarily uses Python and Markdown.

| Technology                     | Purpose                                                                                    |
| ------------------------------ | ------------------------------------------------------------------------------------------ |
| Python                         | Implementing mathematical procedures and numerical algorithms.                             |
| Markdown                       | Writing mathematical theory, derivations, algorithms, and worked examples.                 |
| SymPy                          | Symbolic mathematics and analytical computations.                                          |
| NumPy                          | Numerical calculations and array operations.                                               |
| SciPy                          | Numerical solution of differential equations.                                              |
| Matplotlib                     | Visualization of functions, direction fields, and solution curves.                         |
| Git and GitHub                 | Version control, documentation, project organization, and public presentation of the work. |
| Jupyter Notebook, where useful | Interactive mathematical experiments and computational demonstrations.                     |

Not every tool is required for every topic. The choice depends on the mathematical problem and the learning objective.

---

## 8. Learning Outcomes

After completing the course, I aim to be able to:

1. Define and classify ordinary differential equations using appropriate mathematical terminology.
2. Explain the concepts, assumptions, and properties underlying important ODE methods.
3. Derive important formulas and demonstrate mathematical results where appropriate.
4. Identify suitable methods for solving different classes of differential equations.
5. Solve standard ODE problems manually with clear mathematical reasoning.
6. Formulate differential equations from suitable real-world situations.
7. Analyze initial value problems and understand the conditions associated with existence and uniqueness.
8. Implement selected mathematical and numerical methods independently in Python.
9. Use scientific Python libraries to solve and investigate differential equations.
10. Visualize and interpret analytical and numerical solutions.
11. Verify computational results and evaluate numerical errors.
12. Compare analytical methods, independent implementations, and library-based approaches.
13. Explain the mathematical reasoning behind a computational result.
14. Apply the acquired knowledge to examination problems, further mathematical study, and computational projects.

---

## 9. Intended Audience

This repository is primarily intended for:

* Undergraduate Applied Mathematics students studying ordinary differential equations.
* Students preparing for university examinations in differential equations.
* Learners seeking to strengthen their analytical problem-solving skills.
* Students interested in mathematical computation and scientific programming.
* Researchers and learners who want a structured introduction to analytical and numerical ODE methods.

Although the repository is being developed as part of my own academic preparation, I intend to organize the material clearly enough to serve as a useful learning resource for other students.

---

## 10. How to Use This Repository

For each topic, the recommended learning sequence is:

**Step 1: Study the theory.**

Read `theory.md` to understand the concepts, definitions, assumptions, and derivations.

**Step 2: Understand the algorithm.**

Read `algorithm.md` to learn how to apply the mathematical method systematically.

**Step 3: Work through the examples.**

Study `example.md`, follow the calculations, and independently solve the examples before checking the results.

**Step 4: Implement the method.**

Study `code1.py` to understand how the mathematical procedure is translated into Python.

**Step 5: Explore library-based computation.**

Study `code2.py` to see how established scientific libraries can be used to solve the problem.

**Step 6: Compare and verify.**

Compare the mathematical, manual, and computational results wherever possible. Investigate any differences rather than assuming that every output is correct.

**Step 7: Practice independently.**

Attempt additional exercises without consulting the solutions. Explain your reasoning, identify the appropriate method, and verify your final answer.

**Step 8: Review and consolidate.**

Return to the theoretical explanations and important formulas, then practice problems that combine multiple concepts.

For examination preparation, particular attention should be given to method selection, derivations, manual calculations, initial conditions, and verification.

For computational development, particular attention should be given to algorithm design, implementation, numerical accuracy, testing, and interpretation.

---

## 11. Future Development

This repository will be developed progressively as I study and practice each topic.

Planned improvements include:

* Completing the theoretical documentation for individual topics.
* Adding carefully selected worked examples.
* Implementing suitable algorithms in Python.
* Adding tests to verify independent implementations.
* Improving visual explanations using graphs and diagrams.
* Comparing analytical and numerical solutions.
* Adding practice problems for examination preparation.
* Documenting computational limitations and numerical errors.
* Including selected mathematical modeling problems.
* Developing integrated projects that combine several ODE concepts.
* Refining the documentation based on further study and testing.

The priority is to develop accurate, understandable, and well-tested material rather than simply increasing the number of files.

---

## 12. Reference

**Primary Reference**

Kreyszig, E., Kreyszig, H., & Norminton, E. J. (2011). *Advanced Engineering Mathematics* (10th ed.). John Wiley & Sons.

The principal ODE material is organized around Chapters 1–6, with selected numerical methods drawn from Chapter 21.

The textbook serves as the primary reference for mathematical concepts, derivations, solution methods, and example selection. The repository will provide original explanations, independently developed examples, Python implementations, and computational experiments to support learning.

**Note:** This repository is an independent educational project. It is not an official publication or an official companion resource of the textbook's authors or publisher.

---

## Final Statement

This project represents my commitment to developing a strong foundation in applied mathematics through a combination of theoretical understanding, analytical problem-solving, algorithmic thinking, and scientific programming.

By connecting mathematical theory with independent implementation and computational verification, I aim to strengthen my preparation for the Ethiopian University Exit Examination while building a portfolio that demonstrates my readiness for further academic study and research.

**The guiding principle of this project is simple: understand the mathematics, derive the method, solve the problem, implement the algorithm, and verify the result.**
