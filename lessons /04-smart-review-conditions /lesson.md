# 🏆 Lesson 04 — Smart Review and Deeper Understanding of Conditions

## What will we learn today?
- Reviewing conditions using `if`, `elif`, and `else`.
- Choosing the largest value among several values.
- Understanding the data type using `type()`.

---

## Reviewing conditions:
We can compare three values and find the largest among them:
```python
a = 22
b = 37
c = 5

if a > b and a > c:
    print(a)
elif b > a and b > c:
    print(b)
else:
    print(c)
