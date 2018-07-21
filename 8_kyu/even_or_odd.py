#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Even or Odd: https://www.codewars.com/kata/53da3dbb4a5168369a0000fe"""


def even_or_odd(number):
    return 'Odd' if number & 0b1 else 'Even'
