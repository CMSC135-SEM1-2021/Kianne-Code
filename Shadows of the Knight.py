import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

# w: width of the building.
# h: height of the building.
w, h = [int(i) for i in input().split()]
n = int(input())  # maximum number of turns before game over.
x0, y0 = [int(i) for i in input().split()]
lower_x = 0
lower_y = 0
upper_x = w - 1
upper_y = h - 1

# game loop
while True:
    bomb_dir = input()  # the direction of the bombs from batman's current location (U, UR, R, DR, D, DL, L or UL)

    if "U" in bomb_dir:
        upper_y = y0 - 1
    elif "D" in bomb_dir:
        lower_y = y0 + 1
    if "L" in bomb_dir:
        upper_x = x0 - 1
    elif "R" in bomb_dir:
        lower_x =x0 + 1

    x0 = lower_x + (upper_x  - lower_x)//2
    y0 = lower_y + (upper_y  - lower_y)//2

    print(x0,y0)
