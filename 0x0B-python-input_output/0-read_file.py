#!/usr/bin/python3
"""
    read file function
"""


def read_file(filename=""):
    """
    opemimg file
    """
    with open(filename) as f:
        line = f.read()
        print(line, end="")
