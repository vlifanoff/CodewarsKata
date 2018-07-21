#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Give me a Diamond: https://www.codewars.com/kata/5503013e34137eeeaa001648"""


def diamond(n):
    if (not 0b1 & n) or n < 1:
        return None

    sign = "*"
    result = sign * n + "\n"
    for i in range(n - 2, 0, -2):
        tmp = (' ' * ((n - i) // 2)) + (sign * i) + "\n"
        result = tmp + result + tmp

    return result
