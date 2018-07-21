#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Difference between two collections: https://www.codewars.com/kata/594093784aafb857f0000122"""


def diff(a, b):
    return sorted(set(a).symmetric_difference(set(b)))
