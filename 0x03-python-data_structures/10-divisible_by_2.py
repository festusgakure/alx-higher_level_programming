#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    even = []
    for j in my_list:
        even.append(j % 2 == 0)
    return even
