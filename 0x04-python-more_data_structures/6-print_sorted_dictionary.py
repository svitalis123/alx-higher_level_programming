#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    """
    Prints a dictionary in sorted order
    """
    for key, value in sorted(a_dictionary.items()):
        print("{}: {}".format(key, value))
