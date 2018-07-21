#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Reverse polish notation calculator: https://www.codewars.com/kata/52f78966747862fc9a0009ae"""


def calc(expr):
    expr = expr.split()

    if not expr:
        return 0

    calculator = {
        "+": lambda x, y: x + y,
        "-": lambda x, y: x - y,
        "*": lambda x, y: x * y,
        "/": lambda x, y: x / y
    }

    i = 0
    while i < len(expr):
        if expr[i] in "+-*/":
            tmp = calculator[expr[i]](float(expr[i - 2]), float(expr[i - 1]))
            expr = expr[:i - 2] + [str(tmp)] + expr[i + 1:]
            i = 1
            continue
        i += 1

    result = float(expr[len(expr) - 1])
    return int(result) if result.is_integer() else result
