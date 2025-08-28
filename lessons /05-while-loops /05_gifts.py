# -*- coding: utf-8 -*-
# 05_gifts.py
# Example: Codey gives gifts as long as he has balloons or flowers

balloons = 3
flowers = 2

while balloons > 0 or flowers > 0:
    print("🎁 Codey gives a gift!")
    if balloons > 0:
        balloons -= 1
    elif flowers > 0:
        flowers -= 1

print("🎈 Gifts are over — Balloons:", balloons, "Flowers:", flowers)
