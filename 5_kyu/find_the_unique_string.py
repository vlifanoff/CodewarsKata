#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Find the unique string: https://www.codewars.com/kata/585d8c8a28bc7403ea0000c3"""

from collections import Counter


def find_uniq(arr):
    for k, v in Counter([''.join(set(sorted(x.lower().replace(' ', '')))) for x in arr]).items():
        if v == 1:
            for x in arr:
                if k == ''.join(set(sorted(x.lower().replace(' ', '')))):
                    return x
