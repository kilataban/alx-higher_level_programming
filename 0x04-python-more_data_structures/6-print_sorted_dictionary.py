#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    """print dictionary by ordered keys"""
    [print("{}: {}".format(ky, a_dictionary[ky])) for ky in sorted(a_dictionary)]
