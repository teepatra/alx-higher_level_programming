#!/usr/bin/python3

"""
N Queens puzzle module
"""

import sys
def init_chess(n):
    """Initialize  `n`x`n` chess size with 0's."""
    chess = []
    [chess.append([]) for i in range(n)]
    [row.append(' ') for i in range(n) for row in chess]
    return (chess)
