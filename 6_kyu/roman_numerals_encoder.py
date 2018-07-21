#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Roman Numerals Encoder: https://www.codewars.com/kata/51b62bf6a9c58071c600001b"""

data = [
    (1000, 'M'),
    (900, 'CM'),
    (500, 'D'),
    (400, 'CD'),
    (100, 'C'),
    (90, 'XC'),
    (50, 'L'),
    (40, 'XL'),
    (10, 'X'),
    (9, 'IX'),
    (5, 'V'),
    (4, 'IV'),
    (1, 'I')
]


def solution(n):
    roman_num = ''
    for arab, roman in data:
        while n - arab >= 0:
            n -= arab
            roman_num += roman

    return roman_num
