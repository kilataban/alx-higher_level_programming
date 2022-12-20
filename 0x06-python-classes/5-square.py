#!/usr/bin/python3
# 5-square.py
"""Square class including print method """


class Square(object):
    """class variable size"""
    def __init__(self, size=0):
        """Initiate square size"""
        self.__size = size

    @property
    def size(self):
        """Define self reference property"""
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
        """Define the function to find square area"""
        return self.__size * self.__size

    def my_print(self):
        """Define function that prints square as #"""
        if self.__size > 0:
            for i in range(self.__size):
                for j in range(self.__size):
                    print("#", end="")
                print("")
        else:
            print("")
