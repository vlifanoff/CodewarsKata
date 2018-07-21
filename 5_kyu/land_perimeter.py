#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Land perimeter: https://www.codewars.com/kata/5839c48f0cf94640a20001d3"""


def land_perimeter(arr):
    piece_of_land = 'X'
    cell_perimeter = 4
    exclude_perimeter = 2

    result = 0
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if arr[i][j] == piece_of_land:
                result += cell_perimeter
                if i != 0 and arr[i - 1][j] == piece_of_land:
                    result -= exclude_perimeter
                if j != 0 and arr[i][j - 1] == piece_of_land:
                    result -= exclude_perimeter

    return "Total land perimeter: {}".format(result)
