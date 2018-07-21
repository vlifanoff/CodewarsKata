#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Delete occurrences of an element if it occurs more than n times:
https://www.codewars.com/kata/554ca54ffa7d91b236000023"""


def delete_nth(order, max_e):
    return [x for i, x in enumerate(order) if order[:i].count(x) < max_e]
