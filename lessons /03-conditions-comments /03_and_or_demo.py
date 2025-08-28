# -*- coding: utf-8 -*-
# 03_and_or_demo.py
# Examples of and and or

age = int(input("How old are you? "))
has_ticket = input("Do you have a ticket? (yes/no) ") == "yes"

# Using and
if age >= 18 and has_ticket:
    print("✅ You can enter")
else:
    print("❌ You cannot enter")

# Using or
is_member = input("Are you a member? (yes/no) ") == "yes"
if age >= 18 or is_member:
    print("🎉 You can join the club")
else:
    print("🚫 Sorry, you cannot join")
