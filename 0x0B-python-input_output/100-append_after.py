#!/usr/bin/python3
"""SearchNdUpdate module"""


def append_after(filename="", search_string="", new_string=""):
    """
    Inserts a line of text to a file, after each line containing a specific string

    Args:
    filename (str): name of the file to be modified
    search_string (str): the string to search for in each line
    new_string (str): the string to be inserted after each line containing the search_string

    Returns:
    None

    """
    with open(filename, 'r+') as file:
         lines = file.readlines()
         file.seek(0)
         for line in lines:
               file.write(line)
               if search_string in line:
                file.write(new_string + '\n')
                file.truncate()
