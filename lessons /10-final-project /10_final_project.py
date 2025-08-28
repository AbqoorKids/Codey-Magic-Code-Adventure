# Lesson 10: Final Project - A Little Programmer Solving Challenges!

# 1. 2D list of items and their space (in square meters)
items = [
    ["Bed", 3],
    ["Desk", 2],
    ["Toys", 2],
    ["Lamp", 1],
    ["Bookshelves", 2],
    ["Helper Robot", 1],
    ["Sofa", 1],
    ["TV", 2],
]

# 2. Display the number of these items
print("Number of available items:", len(items))

# 3. Print these items with their space
print("Available items:")
for piece in items:
    print("-", piece[0], "needs", piece[1], "meters")

# 4. Take 5 choices from the user and store them in a list
print("\nChoose 5 items from the list (type the name exactly as shown):")

choice1 = input("Choice 1: ")
choice2 = input("Choice 2: ")
choice3 = input("Choice 3: ")
choice4 = input("Choice 4: ")
choice5 = input("Choice 5: ")

chosen = [choice1, choice2, choice3, choice4, choice5]

# 5. Calculate the space needed for these items
total_space = 0
for choice in chosen:
    for piece in items:
        if choice == piece[0]:
            total_space = total_space + piece[1]

# 6. Inform the user if the items will fit in the room
print("\nRequired space:", total_space, "square meters")
if total_space > 10:
    print("❌ Not enough space for these items.")
else:
    print("✅ Great! The items can fit in the room.")

# 7. Display the chosen items sorted alphabetically
sorted_items = sorted(chosen)
print("Your chosen items after sorting:")
for item in sorted_items:
    print("-", item)
