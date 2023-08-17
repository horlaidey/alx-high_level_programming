#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is not None:
        keys = list(a_dictionary.keys())
        tmp_best = 0
        best_key = ""
        for i in keys:
            if a_dictionary[i] > tmp_best:
                tmp_best = a_dictionary[i]
                best_key = i
        return best_key
    else:
        return None
