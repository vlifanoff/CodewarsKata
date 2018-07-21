#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Jaden Casing Strings: https://www.codewars.com/kata/5390bac347d09b7da40006f6"""

import re


def toJadenCase(string):
    return ''.join([x.capitalize() for x in re.findall(r'\S+|\s+', string)])
