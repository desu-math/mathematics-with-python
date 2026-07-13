"""
Probability Basics
(NumPy Simulation)

This program demonstrates basic probability concepts
using NumPy.

Author: Desalu Horsa
"""

import numpy as np

# -------------------------------------------------
# Random Number Generator
# -------------------------------------------------

rng = np.random.default_rng()

# -------------------------------------------------
# Coin Toss Simulation
# -------------------------------------------------

number_of_tosses = 1000

coin_tosses = rng.choice(["Head", "Tail"], size=number_of_tosses)

heads = np.count_nonzero(coin_tosses == "Head")
tails = np.count_nonzero(coin_tosses == "Tail")

print("Coin Toss Simulation")
print("-" * 30)

print(f"Number of Tosses : {number_of_tosses}")
print(f"Heads            : {heads}")
print(f"Tails            : {tails}")

print("\nEstimated Probabilities")
print(f"P(Head) = {heads / number_of_tosses:.3f}")
print(f"P(Tail) = {tails / number_of_tosses:.3f}")

print("\nTheoretical Probabilities")
print("P(Head) = 0.500")
print("P(Tail) = 0.500")

# -------------------------------------------------
# Dice Rolling Simulation
# -------------------------------------------------

number_of_rolls = 6000

dice_rolls = rng.integers(1, 7, size=number_of_rolls)

print("\n\nDice Rolling Simulation")
print("-" * 30)

for face in range(1, 7):

    count = np.count_nonzero(dice_rolls == face)
    probability = count / number_of_rolls

    print(f"Face {face}: {count:4d}   P = {probability:.3f}")

print("\nTheoretical Probability for each face = 1/6 ≈ 0.167")
