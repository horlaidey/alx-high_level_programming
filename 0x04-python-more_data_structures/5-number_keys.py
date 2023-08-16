#!/usr/bin/python3
def number_keys(a_dictionary):
    a_list = []
    for key, value in a_dictionary.items():
        a_list.append(key)
    return len(a_list)
