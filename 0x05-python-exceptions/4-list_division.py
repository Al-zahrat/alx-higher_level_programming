#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    x = []
    for i in range(list_length):
        try:
            b = my_list_1[i] / my_list_2[i]
        except ZeroDivisionError:
            print("division by 0")
            b = 0
        except (TypeError, ValueError):
            print("wrong type")
            b = 0
        except IndexError:
            print("out of range")
            b = 0
        finally:
            x.append(b)
    return x
