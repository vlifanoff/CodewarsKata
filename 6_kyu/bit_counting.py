#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Bit Counting: https://www.codewars.com/kata/526571aae218b8ee490006f4"""


def countBits(n):
    return bin(n).count('1')
