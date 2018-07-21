#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Broken sequence: https://www.codewars.com/kata/5512e5662b34d88e44000060"""


def find_missing_number(seq):
    try:
        for i, x in enumerate(sorted(seq.split(), key=int), 1):
            if str(i) != x:
                return i
    except ValueError:
        return 1

    return 0
