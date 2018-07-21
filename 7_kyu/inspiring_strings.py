#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Inspiring Strings: https://www.codewars.com/kata/5939ab6eed348a945f0007b2"""


def longest_word(string_of_words):
    return sorted(string_of_words.split(), key=len)[-1]
