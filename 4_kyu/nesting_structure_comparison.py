#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Nesting Structure Comparison: https://www.codewars.com/kata/520446778469526ec0000001"""


def same_structure_as(original, other):
    if (not isinstance(other, list) or not isinstance(original, list)) or (len(other) != len(original)):
        return False

    for x in range(len(other)):
        if isinstance(other[x], list) and isinstance(original[x], list):
            if not same_structure_as(other[x], original[x]):
                return False
        elif isinstance(other[x], list) or isinstance(original[x], list):
            return False

    return True
