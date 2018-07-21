#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Counting Duplicates: https://www.codewars.com/kata/54bf1c2cd5b56cc47f0007a1"""


def duplicate_count(text):
    tl = text.lower()
    return sum(1 for x in set(tl) if tl.count(x) > 1)
