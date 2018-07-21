#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Strip Comments: https://www.codewars.com/kata/51c8e37cee245da6b40000bd"""

import re


def solution(string, markers):
    return string if not markers else re.sub(r'[\t ]*[\{}].*'.format('\\'.join(markers)), '', string, re.M | re.S)
