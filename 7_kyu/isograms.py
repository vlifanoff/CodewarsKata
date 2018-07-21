#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""Isograms: https://www.codewars.com/kata/54ba84be607a92aa900000f1"""


def is_isogram(string):
    d = {}
    for s in string.lower():
        if s in d:
            return False
        else:
            d[s] = 1

    return True
