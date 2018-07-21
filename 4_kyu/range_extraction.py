#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""Range Extraction: https://www.codewars.com/kata/51ba717bb08c1cd60f00002f"""


def append_range(result, start, end, counter):
    if counter == 0:
        result.append(str(start))
    elif counter == 1:
        result.append('{},{}'.format(start, end))
    else:
        result.append('{}-{}'.format(start, end))


def solution(args):
    if len(args) == 0:
        return ''
    elif len(args) == 1:
        return str(args[0])

    tmp = sorted(set(args))

    result, start, end, counter = [], tmp[0], tmp[1], 0
    for i in range(len(tmp) - 1):
        if tmp[i] + 1 == tmp[i + 1]:
            counter += 1
            end = tmp[i + 1]
        else:
            append_range(result, start, end, counter)
            counter = 0
            start = tmp[i + 1]

    append_range(result, start, end, counter)

    return ','.join(result)
