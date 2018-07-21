#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Persistent Bugger: https://www.codewars.com/kata/55bf01e5a717a0d57e0000ec"""

from functools import reduce


def persistence(n):
    counter = 0
    while n > 9:
        n = reduce(lambda x, y: x * y, map(int, str(n)))
        counter += 1

    return counter
