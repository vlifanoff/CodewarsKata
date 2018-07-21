#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Simple Fun #30: Strings Construction: https://www.codewars.com/kata/58870402c81516bbdb000088"""

from itertools import cycle


def strings_construction(strng, letters):
    tmp_b = [x for x in letters]

    counter = 0
    for i, x in enumerate(cycle(strng), 1):
        if x in tmp_b:
            tmp_b.remove(x)
            if i % len(strng) == 0:
                counter += 1
        else:
            return counter

    return 0
