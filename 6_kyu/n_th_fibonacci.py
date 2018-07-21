#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""N-th Fibonacci: https://www.codewars.com/kata/522551eee9abb932420004a0"""


def nth_fib(n):
    a, b = 0, 1
    for _ in range(1, n):
        a, b = a + b, a

    return a
