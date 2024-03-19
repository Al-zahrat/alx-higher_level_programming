#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    x = []
    if idx < 0 or len(my_list) <= idx:
        return my_list
    else:
        for i in range(0, len(my_list)):
            if i == idx:
                x.append(element)
            else:
                x.append(my_list[i])
        return x
