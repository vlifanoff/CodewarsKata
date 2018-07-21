#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Sum of positive: https://www.codewars.com/kata/5715eaedb436cf5606000381"""


def positive_sum(arr):
    return sum(x for x in arr if x > 0)
