#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list is not None:
        total = 0
        frequency = 0
        for tup in my_list:
            (weight, score) = tup
            total += (weight * score)
            frequency += score
        return (total/frequency) if frequency > 0 else 0
    else:
        return (0)
