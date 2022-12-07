#!/usr/bin/python3
def roman_to_int(roman_string):
    """convert roman numeral to an integer"""
    if type(roman_string) != str or type(roman_string) == None:
        return (0)
    roman_dictionary = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
    }
    count = 0

    for i in range(len(roman_string)):
        if roman_dictionary.get(roman_string[i], 0) == 0:
            return (0)

        if (i != (len(roman_string) - 1) and
                roman_dictionary[roman_string[i]] < roman_dictionary[roman_string[i + 1]]):
                count += roman_dictionary[roman_string[i]] * -1

        else:
            count += roman_dictionary[roman_string[i]]
    return (count)
