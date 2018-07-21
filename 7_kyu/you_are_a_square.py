#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""You're a square!: https://www.codewars.com/kata/54c27a33fb7da0db0100040e"""

import math


def is_square(n):
    if n < 1:
        return False

    tmp = int(math.sqrt(n))
    return True if n / tmp == tmp else False
