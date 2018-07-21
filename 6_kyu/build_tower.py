#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Build Tower: https://www.codewars.com/kata/576757b1df89ecf5bd00073b"""


def tower_builder(n_floors):
    l = []
    size = n_floors * 2 - 1

    for i in range(1, n_floors + 1):
        d = i * 2 - 1
        ws = ' ' * ((size - d) / 2)
        l.append(ws + ('*' * d) + ws)

    return l
