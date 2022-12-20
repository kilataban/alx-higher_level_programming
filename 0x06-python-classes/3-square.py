#!/usr/bin/python3
# 3-square.py
"""Add method that determines square area """


class Square(object):
    """class var size"""
    def __init__(self, size=0):
        """Method that initialises the class instance"""
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Define area method with private instances"""
        return self.__size * self.__size
