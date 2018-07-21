#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Where my anagrams at?: https://www.codewars.com/kata/523a86aa4230ebb5420001e1"""


def anagrams(word, words):
    sword = ''.join(sorted(word))
    h = {x: ''.join(sorted(x)) for x in words}
    return [x for x in words if h[x] == sword]
