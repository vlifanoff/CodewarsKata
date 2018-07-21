#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Count all the sheep on farm in the heights of New Zealand: https://www.codewars.com/kata/58e0f0bf92d04ccf0a000010"""


def lostSheep(friday, saturday, total):
    return total - sum(friday + saturday)
