#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tribonacci Sequence: https://www.codewars.com/kata/556deca17c58da83c00002db"""


def tribonacci(signature, n):
    magic_number = 3

    if (len(signature) < magic_number):
        return signature

    if (n < 0):
        return []
    elif (n < magic_number):
        return signature[:n]
    else:
        while n > magic_number:
            signature.append(sum(signature[-magic_number:]))
            n -= 1

    return signature
