#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Is this a triangle?: https://www.codewars.com/kata/56606694ec01347ce800001b"""


def is_triangle(a, b, c):
    if (all(x > 0 for x in [a, b, c])):
        a, b, c = sorted([a, b, c])
        return a + b > c
    else:
        return False
