#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    """print dictionary by ordered keys"""
    [print("{}: {}".format(keys, a_dictionary[keys])) for keys in sorted(a_dictionary)]
