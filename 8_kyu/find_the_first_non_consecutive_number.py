#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Find the first non-consecutive number: https://www.codewars.com/kata/58f8a3a27a5c28d92e000144"""


def first_non_consecutive(arr):
    if not arr:
        return None

    for i, x in enumerate(arr, arr[0]):
        if i != x:
            return x

    return None
