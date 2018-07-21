#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Sort the odd: https://www.codewars.com/kata/578aa45ee9fd15ff4600090d"""


def sort_array(source_array):
    is_odd = lambda x: x & 0b1
    odds = sorted(filter(is_odd, source_array), reverse=True)
    return [odds.pop() if is_odd(source_array[i]) else source_array[i] for i in range(len(source_array))]
