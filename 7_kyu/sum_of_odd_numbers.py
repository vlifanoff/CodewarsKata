#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Sum of odd numbers: https://www.codewars.com/kata/55fd2d567d94ac3bc9000064"""


def row_sum_odd_numbers(n):
    total_odds = sum(range(1, n + 1))
    return sum(range(total_odds * 2 - 1, total_odds * 2 - n * 2, -2))
