#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Remove the minimum: https://www.codewars.com/kata/563cf89eb4747c5fb100001b"""


def remove_smallest(numbers):
    if not numbers:
        return []
    tmp = numbers[:]
    tmp.remove(min(numbers))
    return tmp
