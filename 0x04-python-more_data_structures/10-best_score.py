#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    else:
        mx = 0
        key = ""
        for k, v in a_dictionary.items():
            if v > mx:
                mx = v
                key = k
        return key
