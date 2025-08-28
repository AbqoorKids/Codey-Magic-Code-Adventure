# -*- coding: utf-8 -*-
# 05_circles.py
# Example: Playing a loop until Abqoor wins the teddy bear (needs 3 attempts)

circles_count = 0

while circles_count < 3:
    print("🎯 Play again — Attempt number:", circles_count + 1)
    circles_count = circles_count + 1  # or circles_count += 1

print("🎉 Congratulations! You won the teddy bear")
