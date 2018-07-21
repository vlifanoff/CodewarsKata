#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""RGB To Hex Conversion: https://www.codewars.com/kata/513e08acc600c94f01000001"""


def rgb2hex(n):
    if n < 0:
        n = 0
    elif n > 255:
        n = 255

    return '{:02X}'.format(n)


def rgb(r, g, b):
    return '{}{}{}'.format(rgb2hex(r), rgb2hex(g), rgb2hex(b))
