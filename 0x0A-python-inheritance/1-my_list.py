#!/usr/bin/python3
"""
Module contains one function
"""


class MyList(list):
    """
    Class contains one  method
    """
    def print_sorted(self):
        """
        MyList that inherits from list
        """
        sorted_list = sorted(self)
        print(sorted_list)
