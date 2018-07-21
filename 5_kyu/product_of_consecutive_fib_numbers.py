#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Product of consecutive Fib numbers: https://www.codewars.com/kata/5541f58a944b85ce6d00006a"""


def productFib(n):
    a, b = 0, 1

    while True:
        a, b = b, a + b

        z = a * b
        if z == n:
            return [a, b, True]
        elif z > n:
            return [a, b, False]
