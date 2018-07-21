#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Vowel Count: https://www.codewars.com/kata/54ff3102c1bad923760001f3"""


def getCount(inputStr):
    num_vowels = 0

    for l in inputStr:
        if l in "aeiou":
            num_vowels += 1

    return num_vowels
