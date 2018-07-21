#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Partial Word Searching: https://www.codewars.com/kata/54b81566cd7f51408300022d"""


def word_search(query, seq):
    res = [x for x in seq if query.lower() in x.lower()]
    return res if res else ['None']
