#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Exclamation marks series #1: Remove a exclamation mark from the end of string:
https://www.codewars.com/kata/57fae964d80daa229d000126"""


def remove(s):
    if s:
        return s[:-1] if s[-1] == '!' else s
    return ''
