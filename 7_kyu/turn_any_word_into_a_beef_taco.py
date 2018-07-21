#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Turn any word into a beef taco: https://www.codewars.com/kata/59414b46d040b7b8f7000021"""

table = {
    't': 'tomato',
    'l': 'lettuce',
    'c': 'cheese',
    'g': 'guacamole',
    's': 'salsa',
    'a': 'beef',
    'e': 'beef',
    'i': 'beef',
    'o': 'beef',
    'u': 'beef'
}


def tacofy(word):
    return ['shell'] + [table[x] for x in word.lower() if x in table] + ['shell']
