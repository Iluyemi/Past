#!/usr/bin/python3
"""
    py object deserialization function
"""


def load_from_json_file(filename):
    """
    function
    """
    import json
    with open(filename, 'r') as f:
        h = f.read()
        a = json.loads(h)
        return a
