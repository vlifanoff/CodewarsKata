#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Find the capitals: https://www.codewars.com/kata/539ee3b6757843632d00026b"""


def capitals(word):
    return [i for i in range(len(word)) if word[i].isupper()]
