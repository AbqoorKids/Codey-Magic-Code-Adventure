# -*- coding: utf-8 -*-
# 07_trip.py
# Trip list: each country with activities Codey did there

trip = [
    ["United Kingdom", ["Big Ben", "English Tea"]],
    ["France", ["Eiffel Tower", "Croissant"]],
    ["Italy", ["Leaning Tower of Pisa", "Pizza"]],
]

for country_and_activities in trip:
    print("Country:", country_and_activities[0])
    for activity in country_and_activities[1]:
        print("  Activity:", activity)
