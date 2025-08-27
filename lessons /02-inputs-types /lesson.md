# Lesson 02 — Getting Input and Understanding Types 📝

## What will we learn? 🤓
- How to ask the user to enter some data using `input()`.
- That `input()` always gives back a **text (String)**, even if the user types a number.
- How to change text into a number using `int()` (this is called Casting or type conversion).
- How to use `type()` to check the type of a value.
- Fun examples and small mistakes that might happen, and how to fix them.

---

## Important Note ⚠️
The `input()` function makes the program **wait** for the user to type something and press Enter. The result is always **text** — so if you want a number, you need to convert it like this: `age = int(input("How old are you? "))`

If the user types something that is not a number and we try to convert it with int(), you'll get an error (ValueError). 😅

---

##Files in this lesson 📂
- `02_name_age.py` —  Example: ask for name and age, then print a message. 🧒👧

- `02_crowns.py` — Example: is the number of crowns even or odd? 👑

- `02_kangaroo.py` —  Example: is the kangaroo a baby or not? 🦘

- `02_type_demo.py` — Shows type() and int() in action. ⚡

- `02_exercise.md` —  Exercises for practice ✍️


Run each file separately 🏃‍♂️💨
```bash
python3 lessons/02-inputs-types/02_name_age.py
python3 lessons/02-inputs-types/02_crowns.py
python3 lessons/02-inputs-types/02_kangaroo.py
python3 lessons/02-inputs-types/02_type_demo.py
