#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Stop gninnipS My sdroW!: https://www.codewars.com/kata/5264d2b162488dc400000001"""

import re


def spin_words(sentence):
    return ''.join([x if len(x) < 5 else x[::-1] for x in re.findall(r'\S+|\s+', sentence)])
