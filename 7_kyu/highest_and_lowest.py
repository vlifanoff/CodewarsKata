#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Highest and Lowest: https://www.codewars.com/kata/554b4ac871d6813a03000035"""


def high_and_low(numbers):
    arr = [int(x) for x in numbers.split()]
    return "{} {}".format(max(arr), min(arr))
