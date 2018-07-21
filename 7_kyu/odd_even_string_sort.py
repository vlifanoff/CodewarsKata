#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Odd-Even String Sort: https://www.codewars.com/kata/580755730b5a77650500010c"""


def sort_my_string(S):
    odd = ''
    even = ''
    for i, x in enumerate(S):
        if 0b1 & i:
            odd += x
        else:
            even += x
    return '{} {}'.format(even, odd)
