#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""List to Array: https://www.codewars.com/kata/557dd2a061f099504a000088"""


def list_to_array(lst):
    res = []
    while hasattr(lst, 'value'):
        res.append(lst.value)
        lst = lst.next
    return res
