#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Memoized Fibonacci: https://www.codewars.com/kata/529adbf7533b761c560004e5"""


def memo(func):
    mem = {}

    def tmp(n):
        if n not in mem:
            mem[n] = func(n)
        return mem[n]

    return tmp


@memo
def fibonacci(n):
    if n in [0, 1]:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)
