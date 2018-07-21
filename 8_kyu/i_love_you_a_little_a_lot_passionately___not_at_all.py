#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""I love you, a little , a lot, passionately ... not at all: https://www.codewars.com/kata/57f24e6a18e9fad8eb000296"""

phrases = ["I love you",
           "a little",
           "a lot",
           "passionately",
           "madly",
           "not at all"]


def how_much_i_love_you(nb_petals):
    nb_petals -= 1
    return phrases[nb_petals] if nb_petals < len(phrases) else phrases[nb_petals % len(phrases)]
