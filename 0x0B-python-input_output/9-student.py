#!/usr/bin/python3
# 9-student.py
"""Student class defines a student"""


class Student:
    """defines a student"""
    def __init__(self, first_name, last_name, age):
        """set instance variables"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """pull dictionary rep of student instance"""
        return self.__dict__
