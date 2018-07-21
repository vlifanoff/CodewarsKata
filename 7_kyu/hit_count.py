#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Hit Count: https://www.codewars.com/kata/57b6f850a6fdc76523001162"""


def counter_effect(hit_count):
    return [list(range(int(x) + 1)) for x in hit_count]
