#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Caesar Cipher Helper: https://www.codewars.com/kata/526d42b6526963598d0004db"""


class CaesarCipher(object):
    def __init__(self, shift):
        self.shift = divmod(shift, 26)[1] if shift > 25 else shift

    def _coder(self, func, s):
        res = []
        for x in list(s.upper()):
            if x.isalpha():
                tmp = func(ord(x), self.shift)
                if tmp < 65:
                    tmp = 90 - (64 - tmp)
                if tmp > 90:
                    tmp = 64 + (tmp - 90)
                res.append(chr(tmp))
            else:
                res.append(x)

        return ''.join(res)

    def encode(self, s):
        return self._coder(lambda x, y: x + y, s)

    def decode(self, s):
        return self._coder(lambda x, y: x - y, s)
