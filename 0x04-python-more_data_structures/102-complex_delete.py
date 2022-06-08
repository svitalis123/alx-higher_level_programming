#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    """
    Deletes all keys with a given value in a dictionary
    """
    for key in list(a_dictionary.keys()):
        if a_dictionary[key] == value:
            del a_dictionary[key]
    return a_dictionary
