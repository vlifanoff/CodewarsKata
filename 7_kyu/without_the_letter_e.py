#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Without the letter 'E': https://www.codewars.com/kata/594b8e182fa0a0d7fc000875"""


def find_E(s):
    if s:
        res = s.lower().count('e')
        return str(res) if res else 'There is no "e".'
    return s
