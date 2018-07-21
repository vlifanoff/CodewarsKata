#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""ASCII Fun #1: X- Shape: https://www.codewars.com/kata/5906436806d25f846400009b"""


def x(n):
    sym_X = '■'
    matrix = [["□" for _ in range(n)] for _ in range(n)]
    half = n // 2
    matrix[half][half] = sym_X
    for i in range(half):
        matrix[i][i] = sym_X
        matrix[i][-i - 1] = sym_X
        matrix[-i - 1][i] = sym_X
        matrix[-i - 1][-i - 1] = sym_X
    return '\n'.join([''.join(x) for x in matrix])
