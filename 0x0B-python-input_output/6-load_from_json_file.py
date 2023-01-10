#!/usr/bin/python3
# 6-load_from_json_file.py
"""define function that makes an object from a json file"""
import json


def load_from_json_file(filename):
    """create Python Object from json file"""
    with open(filename, "r") as f:
        return json.load(f)
