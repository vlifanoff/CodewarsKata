#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Exclamation marks series #11: Replace all vowel to exclamation mark in the sentence:
https://www.codewars.com/kata/57fb09ef2b5314a8a90001ed"""


def replace_exclamation(s):
    return str().join(['!' if x.lower() in "aeiou" else x for x in s])
