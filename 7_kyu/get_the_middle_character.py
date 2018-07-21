#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Get the Middle Character: https://www.codewars.com/kata/56747fd5cb988479af000028"""


def get_middle(s):
    center = len(s) // 2
    return s[center] if 0b1 & len(s) else s[center - 1:center + 1]
