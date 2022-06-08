#!/usr/bin/python3
def roman_to_int(roman_string):
    """
    Roman to Integer
    """
    r = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    roman_string = roman_string.upper()
    last_value = 0
    result = 0
    for char in roman_string:
        value = r[char]
        result += value
        if value > last_value:
            result -= 2 * last_value
            last_value = value
    return result
