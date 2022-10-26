#!/usr/bin/python3
"""
    py object serialization function
"""


def save_to_json_file(my_obj, filename):
    """
    function
    """
    import json
    with open(filename, 'w') as f:
        json.dump(my_obj, f)
