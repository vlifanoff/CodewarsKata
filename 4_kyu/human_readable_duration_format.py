#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Human readable duration format: https://www.codewars.com/kata/52742f58faf5485cae000b9a"""


def time_format(num, kind):
    return ('{} {}'.format(num, kind) if num == 1 else '{} {}s'.format(num, kind)) if num else ''


def make_result(lst):
    lst = list(filter(lambda x: x != '', lst))

    if len(lst) > 1:
        res = '{} and {}'.format(', '.join(lst[:-1]), lst[-1])
    elif len(lst) == 1:
        res = ''.join(lst)
    else:
        res = 'now'

    return res


def format_duration(seconds):
    m, s = divmod(seconds, 60)
    h, m = divmod(m, 60)
    d, h = divmod(h, 24)
    y, d = divmod(d, 365)

    return make_result([time_format(*x) for x in [(y, 'year'), (d, 'day'), (h, 'hour'), (m, 'minute'), (s, 'second')]])
