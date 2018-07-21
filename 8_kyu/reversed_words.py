#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Reversed Words: https://www.codewars.com/kata/51c8991dee245d7ddf00000e"""


def reverseWords(s):
    return ' '.join(reversed(s.split()))
