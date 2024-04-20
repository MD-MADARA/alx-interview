#!/usr/bin/python3
"""Triangle Triangle"""


def pascal_triangle(n):
    """Triangle"""
    return [[int(digit) for digit in str(11 ** i)] for i in range(n)] \
        if n >= 0 else []
