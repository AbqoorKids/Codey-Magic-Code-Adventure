# -*- coding: utf-8 -*-
# 01_demo.py
# Lesson 1 — Examples: Variables, Conditions, and Math Operations

# Example 1: Is the number even or odd?
number = 10
if number % 2 == 0:
    print("The number", number, "is even.")
if number % 2 != 0:
    print("The number", number, "is odd.")

print("-----")

# Example 2: Changing the value of a variable
apples = 4
apples = apples + 2
print("The number of apples now is:", apples)

# Extra condition example for explanation
# Here we check if apples divided by 2 equals 3
if apples / 2 == 3:
    print("Yes, apples/2 == 3 is true.")
