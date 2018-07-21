#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Descending Order: https://www.codewars.com/kata/5467e4d82edf8bbf40000155"""


def Descending_Order(num):
    return int(str().join(sorted(list(str(num)))[::-1]))
