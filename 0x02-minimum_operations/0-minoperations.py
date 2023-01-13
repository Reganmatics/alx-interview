#!/usr/bin/python3
"""
0. Minimum Operations
"""


def minOperations(n):
    """
    args:
        n -> int

    return -> int
    """
    if n <= 0:
        return 0
    operations = 0
    i = 2
    while i <= n:
        operations += 1
        if n % i == 0:
            n = n / i
        else:
            i += 1
    return operations
