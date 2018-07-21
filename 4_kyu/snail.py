#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Snail: https://www.codewars.com/kata/521c2db8ddc89b9b7a0000c1"""


def snail(array):
    result = []

    flag = False
    for _ in range(len(array[0]) * 2 - 1):
        for x in array:
            for i in range(len(x)):
                if x[i] is not None:
                    if not flag:
                        flag = True
                    result.append(x[i])
                    x[i] = None
                else:
                    if flag:
                        break
            if flag:
                flag = False
                break

        array = list(map(list, zip(*array)))[::-1]

    return result
