#!/usr/bin/python3
"""
UTF-8 Validation
"""


def validUTF8(data):
    """
    data: a list of integers
    Return: True if data is a valid UTF-8
    encoding, else return False
    """
    _bytes = 0

    for i in data:
        if _bytes == 0:
            if i >> 5 == 0b110 or i >> 5 == 0b1110:
                _bytes = 1
            elif i >> 4 == 0b1110:
                _bytes = 2
            elif i >> 3 == 0b11110:
                _bytes = 3
            elif i >> 7 == 0b1:
                return False
        else:
            if i >> 6 != 0b10:
                return False
            _bytes -= 1
    return _bytes == 0
