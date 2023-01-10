#!/usr/bin/python3
# 1-write_file.py
"""define a function to count file lines"""


def write_file(filename="", text=""):
    """return number of characters in a file"""
    with open(filename, encoding="utf-8", mode="w+") as f:
        return f.write(text)
