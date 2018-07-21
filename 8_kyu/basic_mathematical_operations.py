#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Basic Mathematical Operations: https://www.codewars.com/kata/57356c55867b9b7a60000bd7"""


def basic_op(operator, value1, value2):
    return {
        "+": value1 + value2,
        "-": value1 - value2,
        "*": value1 * value2,
        "/": value1 / value2,
    }[operator]
