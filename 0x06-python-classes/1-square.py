#!/usr/bin/python3
# 1-square.py
"""Define second square class"""


class Square:
    """Class that defines a square"""

    def __init__(self, size):
        """Initial values for a new square


        Args:
            size (int): Private instance attribute for square size
        """
        self.__size = size
