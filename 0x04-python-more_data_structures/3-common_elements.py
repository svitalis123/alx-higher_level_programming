#!/usr/bin/python3
def common_elements(set_1, set_2):
    """
    Return a list of common elements between two sets.
    """
    return [x for x in set_1 if x in set_2]
