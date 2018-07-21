#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Next bigger number with the same digits: https://www.codewars.com/kata/55983863da40caa2c900004e"""


def next_bigger(num):
    if num < 10:
        return -1

    tmp = list(str(num))
    try:
        i = max(i for i in range(1, len(tmp)) if tmp[i - 1] < tmp[i])
        j = max(j for j in range(i, len(tmp)) if tmp[j] > tmp[i - 1])
    except ValueError:
        return -1

    tmp[j], tmp[i - 1] = tmp[i - 1], tmp[j]
    tmp[i:] = reversed(tmp[i:])
    return int(''.join(tmp))
