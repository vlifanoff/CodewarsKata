#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""max diff - easy: https://www.codewars.com/kata/588a3c3ef0fbc9c8e1000095"""


def max_diff(lst):
    return max(lst) - min(lst) if lst else 0
