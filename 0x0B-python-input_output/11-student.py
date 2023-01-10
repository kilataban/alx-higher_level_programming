#!/usr/bin/python3
# 11-student.py
"""Student class defines a student"""


class Student:
    """defines a student"""
    def __init__(self, first_name, last_name, age):
        """instantiate student object attributes"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """retrieves a dictionary rep of student"""
        if type(attrs) == list and all(type(elem) == str for elem in attrs):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__

    def reload_from_json(self, json):
        """replaces attributes of the student instance"""
        for key, value in json.items():
            setattr(self, key, value)
