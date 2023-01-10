#!/usr/bin/python3
# 5-save_to_json_file.py
"""define function to write an object to a text file"""
import json


def save_to_json_file(my_obj, filename):
    """write an object to a text file"""
    with open(filename, mode="w") as f:
        json.dump(my_obj, f)
