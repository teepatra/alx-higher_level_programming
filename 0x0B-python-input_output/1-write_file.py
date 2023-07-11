#!/usr/bin/python3
"""WriteFile module"""


def write_file(filename="", text=""):
    """Write a text file and prints it out

    Args:
        filename (str): the filename of the text file

    Returns: length of text

    """
    with open(filename, mode='w', encoding="UTF-8") as file:
        file.write(text)
    return len(text)
