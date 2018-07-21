#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Persistent Bugger: https://www.codewars.com/kata/55bf01e5a717a0d57e0000ec"""

from functools import reduce
from operator import mul


def persistence(n):
    counter = 0
    while n > 9:
        n = reduce(mul, map(int, str(n)))
        counter += 1

    return counter
