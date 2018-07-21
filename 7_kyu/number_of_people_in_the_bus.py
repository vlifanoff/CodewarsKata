#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Number of People in the Bus: https://www.codewars.com/kata/5648b12ce68d9daa6b000099"""


def number(bus_stops):
    res = 0
    for x in bus_stops:
        res += x[0] - x[1]
    return res
