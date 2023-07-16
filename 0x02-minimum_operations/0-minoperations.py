#!/usr/bin/python3
"""Minimum Operations"""


def minOperations(n):
    """minimum number of operations"""
    count = 0
    charss = 1
    clip = 0

    while charss < n:

        if clip == 0:
            clip = charss
            count += 1

        if charss == 1:
            charss += clip
            count += 1
            continue

        remaining = n - charss  
        if remaining < clip:
            return 0

        if remaining % charss != 0:
            charss += clip
            count += 1
        else:
            clip = charss
            charss += clip
            count += 2

    
    if charss == n:
        return count
    else:
        return 0