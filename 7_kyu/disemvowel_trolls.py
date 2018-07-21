#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Disemvowel Trolls: https://www.codewars.com/kata/52fba66badcd10859f00097e"""

import re


def disemvowel(string):
    return re.compile(r"[aeiou]+", re.VERBOSE | re.IGNORECASE | re.DOTALL | re.MULTILINE).sub("", string)
