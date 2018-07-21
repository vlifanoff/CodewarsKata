#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Human Readable Time: https://www.codewars.com/kata/52685f7382004e774f0001f7"""


def make_readable(seconds):
    m, s = divmod(seconds, 60)
    h, m = divmod(m, 60)
    return "{:02d}:{:02d}:{:02d}".format(h, m, s)
