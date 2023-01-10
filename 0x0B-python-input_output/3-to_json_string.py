#!/usr/bin/python3
# 3-to_json_string.py
"""define function that returns json object of a string value"""
import json


def to_json_string(my_obj):
    """return json object of a string value"""
    data = json.dumps(my_obj)
    return data
