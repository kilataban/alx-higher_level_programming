#!/usr/bin/python3
def roman_to_int(roman_string):
    """convert roman numeral to an integer"""
    if (type(roman_string) != str or roman_string is None):
        return (0)
    rom_dic = {
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
        if rom_dic.get(roman_string[i], 0) == 0:
            return (0)

        if (i != (len(roman_string) - 1) and
                rom_dic[roman_string[i]] < rom_dic[roman_string[i + 1]]):
                count += rom_dic[roman_string[i]] * -1

        else:
            count += rom_dic[roman_string[i]]
    return (count)
