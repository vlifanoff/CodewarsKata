#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Text align justify: https://www.codewars.com/kata/537e18b6147aa838f600001b"""


def get_lines(atext, width):
    size = 0
    ltext = []
    tmp = []
    lt = len(atext)
    wtmp = width + 1

    while lt > 0:
        size += len(atext[0]) + 1

        if lt == 1:
            if size > wtmp:
                ltext.append(tmp)
                ltext.append([atext.pop(0)])
            else:
                tmp.append(atext.pop(0))
                ltext.append(tmp)
            lt -= 1
        elif size <= wtmp:
            tmp.append(atext.pop(0))
            lt -= 1
        else:
            ltext.append(tmp)
            size = 0
            tmp = []

    return ltext


def get_whitespaces(ltext, width):
    ws = []

    for x in ltext:
        lt = len(x) - 1
        tmp = []
        if lt > 0:
            tmp = [' ' for __ in range(lt)]
            size = len("".join(x))
            wspaces = width - size - lt

            while wspaces >= lt:
                wspaces -= lt
                tmp = [i + ' ' for i in tmp]

            if wspaces < lt:
                for i in range(wspaces):
                    tmp[i] += ' '
            else:
                wspaces -= lt
                tmp = [i + ' ' for i in tmp]

        tmp.append("\n")
        ws.append(tmp)

    for i in range(len(ws[-1])):
        ws[-1][i] = ' '

    ws[-1][-1] = ''

    return ws


def justify(text, width):
    atext = [x for x in text.split(" ") if x != '']

    ltext = get_lines(atext, width)
    ws = get_whitespaces(ltext, width)

    res = ''
    for i in range(len(ltext)):
        res += "".join(["".join(x) for x in zip(ltext[i], ws[i])])

    return res
