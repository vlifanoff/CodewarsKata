#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Common Denominators: https://www.codewars.com/kata/54d7660d2daf68c619000d95"""

from functools import reduce


def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


def lcm(a, b):
    return a * b // gcd(a, b)


def more_lcm(lst):
    return reduce(lcm, lst)


def convertFracts(lst):
    denominator = more_lcm([x[1] for x in lst])
    return [[(denominator // x[1]) * x[0], denominator] for x in lst]
