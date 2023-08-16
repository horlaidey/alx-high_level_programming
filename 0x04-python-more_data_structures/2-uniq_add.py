#!/usr/bin/python3
def uniq_add(my_list=[]):
    total = 0
    uniq_list = list(set(my_list))
    for i in uniq_list:
        total += i
    return total
