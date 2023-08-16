#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = my_list.copy()
    elem = new_list.index(search)
    new_list.remove(search)
    new_list.insert(elem, replace)
    return new_list
