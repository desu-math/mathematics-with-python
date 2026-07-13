
"""
Probability Basics
(Manual Simulation)

This program demonstrates basic probability concepts
using Python's built-in random module.

Author: Desalu Horsa
"""

import random

# -------------------------------------------------
# Coin Toss Simulation
# -------------------------------------------------

number_of_tosses = 1000

heads = 0
tails = 0

for _ in range(number_of_tosses):

    toss = random.choice(["Head", "Tail"])

    if toss == "Head":
        heads += 1
    else:
        tails += 1

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

frequency = {}

for face in range(1, 7):
    frequency[face] = 0

for _ in range(number_of_rolls):

    roll = random.randint(1, 6)

    frequency[roll] += 1

print("\n\nDice Rolling Simulation")
print("-" * 30)

for face in range(1, 7):
    probability = frequency[face] / number_of_rolls
    print(f"Face {face}: {frequency[face]:4d}   P = {probability:.3f}")

print("\nTheoretical Probability for each face = 1/6 ≈ 0.167")

