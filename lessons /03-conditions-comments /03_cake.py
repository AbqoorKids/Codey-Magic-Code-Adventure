# -*- coding: utf-8 -*-
# 03_cake.py
# Example: Compound conditions with and
# Preheat the oven to 180°C

temperature = int(input("What is the temperature? "))
time = int(input("How many minutes? "))

if temperature >= 180 and time >= 20:
    print("🍰 The cake is ready!")
else:
    print("⏳ Not ready yet")
