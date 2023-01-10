#!/usr/bin/python3
# 0-read_file.py
"""define text file-reading function."""


def read_file(filename=""):
    """print file contents to std output"""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
