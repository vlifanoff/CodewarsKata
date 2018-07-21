#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Powers of 2: https://www.codewars.com/kata/57a083a57cb1f31db7000028"""


def powers_of_two(n):
    return [1 << x for x in range(n + 1)]
