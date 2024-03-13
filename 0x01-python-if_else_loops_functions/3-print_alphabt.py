#!/usr/bin/python3
alphc = 97
while alphc <= 122:
    if alphc == 101 or alphc == 113:
        alphc += 1
        continue
    else:
        x = chr(alphc)
        alphc += 1
    print("{}".format(x), end="")
