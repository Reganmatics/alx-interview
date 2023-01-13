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
    ops = [0]*n
    ops[0] = 1
    for i in range(1, n):
        ops[i] = ops[i-1] + 1
        if i % 2 != 0:
            ops[i] = min(ops[i], ops[i // 2] + 1)
    return ops[-1]
