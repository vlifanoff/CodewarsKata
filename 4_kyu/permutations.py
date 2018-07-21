#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Permutations: https://www.codewars.com/kata/5254ca2719453dcc0b00027d"""

from itertools import permutations as prmts


def permutations(s):
    return map(''.join, set(prmts(s)))
