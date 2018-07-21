#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Even Odd Pattern #1: https://www.codewars.com/kata/559e708e72d342b0c900007b"""


def even_odd(arr):
    res = arr[0] if arr else 0

    for i in range(1, len(arr)):
        if 0b1 & i:
            res *= arr[i]
        else:
            res += arr[i]

    return res
