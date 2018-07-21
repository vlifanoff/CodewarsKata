#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Unique In Order: https://www.codewars.com/kata/54e6533c92449cc251001667"""


def unique_in_order(iterable):
    if len(iterable) < 2:
        return list(iterable)

    result = [iterable[0]]
    for i in range(1, len(iterable)):
        if iterable[i] != iterable[i - 1]:
            result.append(iterable[i])

    return result
