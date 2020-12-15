#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    mul2 = my_list.copy()
    for i in range(0, len(my_list)):
        if my_list[i] % 2 == 0:
            mul2[i] = True
        else:
            mul2[i] = False
    return mul2
