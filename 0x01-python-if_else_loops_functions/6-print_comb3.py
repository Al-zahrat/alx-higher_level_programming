#!/usr/bin/python3
for i in range(9):
    j = i + 1
    while j <= 9:
        print("{}{}".format(i, j), end=", " if i < 8 else "\n")
        j += 1
