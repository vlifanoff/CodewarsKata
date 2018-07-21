#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Calculate average: https://www.codewars.com/kata/57a2013acf1fa5bfc4000921"""


def find_average(array):
    return sum(array) / len(array) if len(array) != 0 else 0
