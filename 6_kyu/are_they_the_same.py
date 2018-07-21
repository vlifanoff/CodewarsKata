#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Are they the "same"?: https://www.codewars.com/kata/550498447451fbbd7600041c"""


def comp(array1, array2):
    return array1 is not None and array2 is not None and sorted([x ** 2 for x in array1]) == sorted(array2)
