#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Format a string of names like 'Bart, Lisa & Maggie': https://www.codewars.com/kata/53368a47e38700bd8300030d"""


def namelist(names):
    if not names:
        return ''

    only_names = [x['name'] for x in names]
    if len(only_names) == 1:
        return only_names[0]
    elif len(only_names) == 2:
        return '{} & {}'.format(*only_names)
    else:
        return '{} & {}'.format(', '.join(only_names[:-1]), only_names[-1])
