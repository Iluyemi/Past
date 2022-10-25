#!/usr/bin/python3
"""
    py object serialization function
"""


def to_json_string(my_obj):
    """
    function
    """
    import json
    hi = json.dumps(my_obj)
    return hi
