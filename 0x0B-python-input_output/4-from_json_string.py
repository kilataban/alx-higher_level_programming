#!/usr/bin/python3
# 4-from_json_string.py
"""define function that returns python object"""
import json


def from_json_string(my_str):
    """returns python object/DS"""
    data = json.loads(my_str)
    return data
