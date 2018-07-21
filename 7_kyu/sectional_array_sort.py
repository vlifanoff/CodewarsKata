#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Sectional Array Sort: https://www.codewars.com/kata/58ef87dc4db9b24c6c000092"""


def sect_sort(array, start=0, length=None):
    length = start + length if length else len(array)
    return array[0:start] + sorted(array[start:length]) + array[length:]
