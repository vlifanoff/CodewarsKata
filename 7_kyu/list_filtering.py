#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""List Filtering: https://www.codewars.com/kata/53dbd5315a3c69eed20002dd"""


def filter_list(l):
    return [x for x in l if isinstance(x, int)]
