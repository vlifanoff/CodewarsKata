#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Least Common Multiple: https://www.codewars.com/kata/5259acb16021e9d8a60010af"""

from functools import reduce


def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


def two_lcm(a, b):
    return a * b // gcd(a, b)


def lcm(*args):
    return reduce(two_lcm, args) if len(args) > 1 else args[0]
