#!/usr/bin/python3
"""Contains one module"""


def read_file(filename=""):
    """
    function reads a text file
    """
    with open(filename, encoding="UTF8") as f:
        lines = f.read()
    print(lines, end="")
    f.close()
