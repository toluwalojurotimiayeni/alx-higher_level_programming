#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    multiple = my_list.copy()
    for i in range(0, len(my_list)):
        if my_list[i] % 2 == 0:
            multiple[i] = 1
        else:
            multiple[i] = 0
    return multiple
