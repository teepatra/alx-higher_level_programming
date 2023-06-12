#!/usr/bin/python3
def element_at(my_list, idx):
    """
    Retrieves elements from a list

    Args:
    my_list: provided list
    idx: index position

    Returns:
    None: if idx is negative or out of range
    Item of index: if success
    """

    if idx < 0 or idx > len(my_list) - 1:
        return none
    else:
        return my_list[idx]
