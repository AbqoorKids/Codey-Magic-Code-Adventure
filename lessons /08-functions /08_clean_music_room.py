# -*- coding: utf-8 -*-
# 08_clean_music_room.py
# Function that cleans the music room and calls another function to clean the shelves

def clean_music_room():
    # Print task of watering the plants
    print("Watering the plants")
    # Call the function responsible for cleaning the shelves
    clean_shelves()

def clean_shelves():
    # Repeat 3 times
    for shelf in range(1, 4):
        print("Clean shelf number", shelf)

# Call the main function
clean_music_room()
