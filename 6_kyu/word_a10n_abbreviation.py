#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Word a10n (abbreviation): https://www.codewars.com/kata/5375f921003bf62192000746"""

import re


def make_abbreviate(s):
    g = s.group(0)
    return g if len(g) < 4 else g[0] + str(len(g[1:-1])) + g[-1]


def abbreviate(s):
    return re.sub(r"\b([a-z]+)\b", make_abbreviate, s, 0, re.I)
