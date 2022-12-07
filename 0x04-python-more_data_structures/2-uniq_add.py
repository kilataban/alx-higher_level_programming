#!/usr/bin/python3

def uniq_add(my_list=[]):
    """Add all unique integers in a list one time"""
    result = 0
    for number in set(my_list):
        result += number
    return (result)
