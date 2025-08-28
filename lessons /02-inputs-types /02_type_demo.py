# -*- coding: utf-8 -*-
# 02_type_demo.py
# Show the type of values and why we need int()

name = input("Write your name: ")
print("The type of name is:", type(name))

age_text = input("Write a number, for example 7: ")
print("The type of age_text is:", type(age_text), "Value:", age_text)

# Now we convert the text to an integer
age = int(age_text)
print("After conversion:")
print("The type of age is:", type(age), "and its value is:", age)
