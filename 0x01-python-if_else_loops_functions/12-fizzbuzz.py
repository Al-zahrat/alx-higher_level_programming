#!/usr/bin/python3
def fizzbuzz():
    x = "Fizz"
    y = "Buzz"
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            print(f"{x}{y}", end=" ")
        elif i % 3 == 0:
            print(x, end=" ")
        elif i % 5 == 0:
            print(y, end=" ")
        else:
            print(i, end=" ")
