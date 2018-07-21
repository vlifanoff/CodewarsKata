#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Array.diff: https://www.codewars.com/kata/523f5d21c841566fde000009"""


def array_diff(a, b):
    for x in set(b):
        a = list(filter(lambda c: c != x, a))

    return a
