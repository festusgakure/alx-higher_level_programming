#!/usr/bin/python3
'''
Module containing one function
'''


def add_integer(a, b=98):
    '''
    Function that adds two inegers

    args:a and b which are to be summed

    returns: int: The sum of a and b
    '''
    if type(a) is not int and type(a) is not float:
        raise TypeError("a must be an integer")
    if type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")
    a = int(a)
    b = int(b)

    return(a + b)
