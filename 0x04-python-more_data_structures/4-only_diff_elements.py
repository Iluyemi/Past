#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    set_common = set_1 ^ set_2
    return set_common
