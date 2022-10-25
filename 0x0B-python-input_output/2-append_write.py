#!/usr/bin/python3
"""
    write file function
"""


def append_write(filename="", text=""):
    """
    appending and write
    """
    try:
        with open(filename, 'a') as f:
            return f.write(text)
    except FileNotFoundError:
        with open(filename, 'x') as f:
            return f.write(text)
