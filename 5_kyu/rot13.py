#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Rot13: https://www.codewars.com/kata/530e15517bc88ac656000716"""

from codecs import encode as _dont_use_this_

abc = [chr(x) for x in range(ord('a'), ord('a') + 26)]


def rot13(message):
    result = []

    for x in message:
        if x.isalpha():
            new_num_pos = abc.index(x.lower()) + 13
            new_num_pos = new_num_pos - 26 if new_num_pos >= 26 else new_num_pos
            x = abc[new_num_pos].upper() if x.isupper() else abc[new_num_pos]

        result.append(x)

    return str().join(result)
