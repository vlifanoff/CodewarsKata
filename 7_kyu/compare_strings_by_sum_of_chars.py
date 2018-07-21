#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Compare Strings by Sum of Chars: https://www.codewars.com/kata/576bb3c4b1abc497ec000065"""


def sum_ord(s):
    return sum(map(ord, [x for x in s.upper() if s.isalpha()]))


def compare(s1, s2):
    return sum_ord(s1) == sum_ord(s2) if s1 and s2 else True
