#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    dict_key = sorted(a_dictionary)
    for i in dict_key:
        print("{:s}: {}".format(i, a_dictionary[i]))
