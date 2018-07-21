#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The fusc function -- Part 1: https://www.codewars.com/kata/570409d3d80ec699af001bf9"""


def fusc(n):
    if n < 2:
        return n

    return fusc(n // 2) + fusc(n // 2 + 1) if 0b1 & n else fusc(n // 2)
