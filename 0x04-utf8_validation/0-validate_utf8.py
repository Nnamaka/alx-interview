#!/usr/bin/python3
"""UTF-8 Validation"""


def validUTF8(data):
    """determines if a given data set represents a valid UTF-8 encoding"""
    no_byte = 0

    for i in data:
        if no_byte == 0:
            if i >> 5 == 0b110 or i >> 5 == 0b1110:
                no_byte = 1
            elif i >> 4 == 0b1110:
                no_byte = 2
            elif i >> 3 == 0b11110:
                no_byte = 3
            elif i >> 7 == 0b1:
                return False
        else:
            if i >> 6 != 0b10:
                return False
            no_byte -= 1

    return no_byte == 0
