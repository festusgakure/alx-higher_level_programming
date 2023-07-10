#!/usr/bin/python3
"""
Module containing one function
"""


def lookup(obj):
    """
    Function that returns the list of
    attributes and methods of an object:
    """
    return [attr for attr in dir(obj)]
