#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Prefill an Array: https://www.codewars.com/kata/54129112fb7c188740000162"""


def prefill(n, v=[]):
    if isinstance(n, (str, bytes)):
        if n.isdigit():
            n = int(n)
        else:
            raise TypeError('{} is invalid'.format(n))
    elif isinstance(n, float) or n is None:
        raise TypeError('{} is invalid'.format(n))

    return [v for _ in range(n)]
