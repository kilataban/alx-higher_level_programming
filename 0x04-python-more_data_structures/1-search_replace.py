#!/usr/bin/python3

def search_replace(my_list, search, replace):
    """Replacing all occurences of an element by another in a new list"""
    new_list = my_list[:]
    for a in range(len(new_list)):
        if new_list[a] == search:
            new_list[a] = replace
    return(new_list)
