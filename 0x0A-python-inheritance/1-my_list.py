#!/usr/bin/python3
"""
MyList module
"""
class MyList(list):
    """ a subclass of list base class"""
    def print_sorted(self):
        """print a sorted list"""
        print(sorted(self))
