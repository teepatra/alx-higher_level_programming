#!/usr/bin/python3

def lookup(obj):
    """
    Returns a list of the names of the attributes and methods of an object.

    Parameters:
    obj (object): The object whose attributes and methods to list.

    Returns:
    list: A list of strings representing the names of the attributes and methods of the object.
    """
    return dir(obj)
