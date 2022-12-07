#!/usr/bin/python3

def multiply_by_2(a_dictionary):
    """returns new dictionary will values multiplied by 2"""
    mult_dict = {k: a_dictionary[k] * 2 for k in a_dictionary}
    return mult_dict
