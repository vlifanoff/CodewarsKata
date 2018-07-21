#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Valid Braces: https://www.codewars.com/kata/5277c8a221e209d3f6000b56"""

from collections import deque


def validBraces(string):
    braces = {'(': ')', '[': ']', '{': '}'}
    stack = deque([])

    for s in list(string):
        if len(stack) == 0 or (s in braces.keys()):
            stack.append(s)
        elif s != braces[stack.pop()]:
            return False

    return not bool(len(stack))
