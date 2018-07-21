#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Sum without highest and lowest number: https://www.codewars.com/kata/576b93db1129fcf2200001e6"""


def sum_array(arr):
    return 0 if arr is None or len(arr) < 2 else sum(sorted(arr)[1:-1])
