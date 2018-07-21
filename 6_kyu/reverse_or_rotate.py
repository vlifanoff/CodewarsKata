#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Reverse or rotate?: https://www.codewars.com/kata/56b5afb4ed1f6d5fb0000991"""


def revrot(s, sz):
    if sz < 1:
        return ''

    tmp = [s[x:x + sz] for x in range(0, len(s), sz) if len(s[x:x + sz]) == sz]

    for i in range(len(tmp)):
        if 0b1 & sum(int(x) ** 3 for x in tmp[i]):
            tmp[i] = tmp[i][1:] + tmp[i][0]
        else:
            tmp[i] = tmp[i][::-1]

    return ''.join(tmp)
