#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Remove duplicates from list: https://www.codewars.com/kata/57a5b0dfcf1fa526bb000118"""


def distinct(seq):
    # return list(set(seq))

    result = []
    for x in seq:
        if x not in result:
            result.append(x)

    return result
