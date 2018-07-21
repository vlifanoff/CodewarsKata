#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""String incrementer: https://www.codewars.com/kata/54a91a4883a7de5d7800009c"""

import re


def increment_string(s):
    renum = re.search("(\d+)$", s)

    if renum:
        num = renum.group(1)
        return s[:len(s) - len(num)] + str(int(num) + 1).zfill(len(num))
    else:
        return s + '1'
