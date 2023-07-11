#!/usr/bin/python3
"""Module to_json_string"""
import json

def to_json_string(my_obj):
    """
    Returns the JSON representation of an object.

    Args:
        my_obj: The object to be converted to JSON.

    Returns:
        A string representing the JSON data.

    """
    return json.dumps(my_obj)
