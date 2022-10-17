#!/usr/bin/python3

def add_integer(a, b=98):
    """addition of integers"""
    try:
        a = int(a)
    except (ValueError, TypeError):
       raise TypeError("a must be an integer")
    try:
        b = int(b)
    except (ValueError, TypeError):
       raise TypeError("b must be an integer")
    return a + b