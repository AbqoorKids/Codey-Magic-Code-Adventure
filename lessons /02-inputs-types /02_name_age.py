# -*- coding: utf-8 -*-
# 02_name_age.py
# Example: Ask for the name and age and use int() to convert the age to a number

name = input("What is your name? ")
age = int(input("How old are you? "))

if age <= 10:
    print("Can you play with me,", name, "?")
else:
    print("Nice to meet you,", name, "!")
