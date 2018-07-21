#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Sum of Digits / Digital Root: https://www.codewars.com/kata/541c8630095125aba6000c00"""


def digital_root(n):
    return digital_root(sum(map(int, list(str(n))))) if n > 9 else n
