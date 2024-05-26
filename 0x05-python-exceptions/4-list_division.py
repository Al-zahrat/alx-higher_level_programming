#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    if (my_list_1) and (my_list_2):
        x = []
        for i in range(list_length):
            b = 0
            try:
                b = my_list_1[i] / my_list_2[i]
            except ZeroDivisionError:
                print("division by 0")
            except TypeError:
                print("wrong type")
            except IndexError:
                print("out of range")
            finally:
                x.append(b)
        return x
