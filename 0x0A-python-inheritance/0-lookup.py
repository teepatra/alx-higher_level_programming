#!/usr/bin/python3
"""Module to lookup for available methds"""

def lookup(obj):
    """
    Returns a list of the names of the attributes and methods of an object.

    Args:
    obj (object): The object whose attributes and methods to list.

    Returns:
    (list): A list of object.
    """
    return dir(obj)
