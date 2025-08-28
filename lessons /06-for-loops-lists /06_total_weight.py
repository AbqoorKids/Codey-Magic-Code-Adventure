# -*- coding: utf-8 -*-
# 06_total_weight.py
# Summing the weights of 3 fish entered by the user using for

total_weight = 0

for _fish in range(3):
    # Try to convert the input to an integer — if the user types text, it will cause an error
    weight = int(input("Enter the weight of the fish (in kg): "))
    total_weight = total_weight + weight  # or total_weight += weight

print("Total =", total_weight)
