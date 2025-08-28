# -*- coding: utf-8 -*-
# 07_souvenirs.py
# Codey's friends and each one's souvenirs

souvenirs = [
    ["Luna", ["Shoes", "Bag"]],
    ["Max", ["Glasses", "Scarf"]],
    ["Zara", ["Hat", "Shirt"]]
]

for row in souvenirs:
    # Print friend's name
    print("Friend:", row[0])
    # Iterate over each souvenir
    for souvenir in row[1]:
        print("  Souvenir:", souvenir)
