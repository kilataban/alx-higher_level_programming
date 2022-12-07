#!/usr/bin/python3

def only_diff_elements(set_1, set_2):
    """return set of all elements present in only one set"""
    ret_diff = set_1 ^ set_2
    return(ret_diff)
