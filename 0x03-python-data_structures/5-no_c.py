#!/usr/bin/python3
def no_c(my_string):
    new_string = [rem for rem in my_string if rem != 'C' and rem != 'c']
    return ("".join(new_string))
