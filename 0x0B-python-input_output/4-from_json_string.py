#!/usr/bin/python3
"""
    py object deserialization function
"""


def from_json_string(my_str):
    """
    function
    """
    import json
    hi = json.load(my_str)
    return hi
