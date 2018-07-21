#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Did you mean ...?: https://www.codewars.com/kata/5259510fc76e59579e0009d4"""


class Dictionary:
    def __init__(self, words):
        self.words = words

    def _distance(self, a, b):
        n, m = len(a), len(b)
        if n > m:
            a, b = b, a
            n, m = m, n

        current_row = range(n + 1)
        for i in range(1, m + 1):
            previous_row, current_row = current_row, [i] + [0] * n
            for j in range(1, n + 1):
                add, delete, change = previous_row[j] + 1, current_row[j - 1] + 1, previous_row[j - 1]
                if a[j - 1] != b[i - 1]:
                    change += 1
                current_row[j] = min(add, delete, change)

        return current_row[n]

    def find_most_similar(self, term):
        result = self.words[0]
        min_distance = self._distance(self.words[0], term)

        for x in self.words[1:]:
            tmp = self._distance(x, term)
            if tmp < min_distance:
                min_distance = tmp
                result = x

        return result
