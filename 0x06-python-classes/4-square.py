#!/usr/bin/python3
# 4-square.py
"""Define Square class and update the private size attr """


class Square(object):
    """define the class variables"""
    def __init__(self, size=0):
        """initiate size variable value"""
        self.__size = size

    @property
    def size(self):
        """define size method/property"""
        return self.__size

    @size.setter
    def size(self, value):
        """class variable size"""
        if type(value) != int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Define area method"""
        return self.__size * self.__size
