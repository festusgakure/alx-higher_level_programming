#!/usr/bin/python3
"""Contains one module"""


def write_file(filename="", text=""):
    """
    Writes a string to file and return n of chars written
    """
    with open(filename, 'w', encoding='utf-8') as f:
        return f.write(text)
