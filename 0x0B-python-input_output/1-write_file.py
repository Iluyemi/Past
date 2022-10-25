#!/usr/bin/python3
"""
    write file function
"""


def write_file(filename="", text=""):
    """
    write function
    """
    try:
        with open(filename, 'x') as f:
            return f.write(text)
    except (FileExistsError):
        with open(filename, 'w') as f:
            return f.write(text)
