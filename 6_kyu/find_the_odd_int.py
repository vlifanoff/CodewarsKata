#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Find the odd int: https://www.codewars.com/kata/54da5a58ea159efa38000836"""


def find_it(seq):
    for x in set(seq):
        if 0b1 & seq.count(x):
            return x
