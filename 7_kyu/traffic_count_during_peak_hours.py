#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Traffic Count During Peak Hours: https://www.codewars.com/kata/586ed2dbaa0428f791000885"""


def traffic_count(array):
    return [('{}:00pm'.format(i + 4), n) for i, n in
            enumerate([max(array[x:x + 6]) for x in range(0, len(array), 6) if len(array[x:x + 6]) == 6])]
