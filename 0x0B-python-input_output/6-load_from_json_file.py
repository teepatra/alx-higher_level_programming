#!/usr/bin/python3
"""Module load form json file"""
import json


def load_from_json_file(filename):
    '''
    function that creates an Object from a “JSON file”
    '''
    with open(filename) as filex:
        json_str = filex.read()
        obj = json.loads(json_str)
        return obj
