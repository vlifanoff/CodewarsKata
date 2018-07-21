#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Sum without highest and lowest number: https://www.codewars.com/kata/576b93db1129fcf2200001e6"""


def sum_array(arr):
    if arr == None: return 0
    if len(arr) < 2: return 0
    return sum(sorted(arr)[1:-1])
