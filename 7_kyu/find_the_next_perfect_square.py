#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Find the next perfect square!: https://www.codewars.com/kata/56269eb78ad2e4ced1000013"""

from cmath import sqrt


def find_next_square(sq):
    tmp = sqrt(sq).real

    if tmp - int(tmp) == 0.0:
        return int((tmp + 1) ** 2)

    return -1
