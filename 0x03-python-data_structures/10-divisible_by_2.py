#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    values = []
    for x in range(len(my_list)):
        if my_list[x] % 2 == 0:
            values.append(True)
        else:
            values.append(False)

    return (values)
