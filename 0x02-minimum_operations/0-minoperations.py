#!/usr/bin/python3
"""
Min operations
"""


def minOperations(n):
    if n <= 1:
        return n

    operations = 0
    clipboard = 1        # Initially, there is 1 H character in the clipboard
    current_length = 1   # Length of the string initially

    while current_length < n:
        if n % current_length == 0:
            clipboard = current_length
            operations += 1
        operations += 1      # Paste operation
        current_length += clipboard

    return operations
