#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Split Strings: https://www.codewars.com/kata/515de9ae9dcfc28eb6000001"""


def solution(s):
    res = [s[i:i + 2] for i in range(0, len(s), 2)]
    if len(res) and len(res[-1]) == 1:
        res[-1] += '_'
    return res
