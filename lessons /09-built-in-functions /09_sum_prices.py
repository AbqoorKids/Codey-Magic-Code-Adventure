# -*- coding: utf-8 -*-
# 09_sum_prices.py
# Combining multiple built-in functions

# The list contains the names of toys
toys = ["Roblox", "Gaming Chair", "Wooden Labobo"]

# The list contains the prices of the toys
prices = [50, 150, 80]

# Sum of the prices
sum_prices = sum(prices)

# Number of items
print("Number of items:", len(toys))

# Average price with rounding
print("Average price:", round(sum_prices / len(prices)))
