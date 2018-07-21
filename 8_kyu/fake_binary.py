#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Fake Binary: https://www.codewars.com/kata/57eae65a4321032ce000002d"""

import re


def fake_bin(x):
    return re.compile("[56789]").sub("1", re.compile("[1234]").sub("0", x))
