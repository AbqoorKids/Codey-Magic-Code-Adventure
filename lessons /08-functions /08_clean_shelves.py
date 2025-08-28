# -*- coding: utf-8 -*-
# 08_clean_shelves.py
# Function to clean the shelves

def clean_shelves():
    # Repeat 3 times
    for shelf in range(1, 4):
        # Stops before the last number (won't reach iteration 4)
        print("Clean shelf number", shelf)

# Call the function
clean_shelves()
