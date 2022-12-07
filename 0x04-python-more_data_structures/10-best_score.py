#!/usr/bin/python3
def best_score(a_dictionary):
    """return a key with the biggest integer value."""
    if (type(a_dictionary) != dict) or len(a_dictionary) == 0:
        return None

    ret_val = list(a_dictionary.keys())[0]
    big = a_dictionary[ret_val]
    for k, v in a_dictionary.items():
        if v > big:
            big = v
            ret_val = k
    return (ret_val)
