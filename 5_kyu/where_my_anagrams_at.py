#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Where my anagrams at?: https://www.codewars.com/kata/523a86aa4230ebb5420001e1"""


def anagrams(word, words):
    sw = sorted(word)
    return [x for x in words if sw == sorted(x)]
