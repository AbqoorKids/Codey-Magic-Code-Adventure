# -*- coding: utf-8 -*-
# 05_icecream.py
# Example: Codey eats ice cream as long as he has money and hasn't tried all flavors

money = 3
flavours = 4

while money > 0 and flavours > 0:
    print("🍦 Codey eats ice cream!")
    money -= 1
    flavours -= 1

print("🧾 Money left:", money, " | Flavors left:", flavours)
if money <= 0 or flavours <= 0:
    print("⏳ He can't try more now.")
