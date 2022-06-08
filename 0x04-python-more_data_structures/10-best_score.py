#!/usr/bin/python3
def best_score(a_dictionary):
    """
    Prints the key with the highest value
    """
    if a_dictionary is None or len(a_dictionary) == 0:
        return None
    max_value = max(a_dictionary.values())
    for key, value in a_dictionary.items():
        if value == max_value:
            return key
