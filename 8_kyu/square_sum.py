#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Square(n) Sum: https://www.codewars.com/kata/515e271a311df0350d00000f"""


def square_sum(numbers):
    return sum(map(lambda x: x ** 2, numbers))
