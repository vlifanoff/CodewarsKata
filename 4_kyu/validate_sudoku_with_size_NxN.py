#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Validate Sudoku with size 'NxN': https://www.codewars.com/kata/540afbe2dc9f615d5e000425"""

from math import sqrt
from copy import deepcopy
from itertools import chain
from functools import reduce
from operator import mul


class IValid(object):
    def is_valid(self):
        raise NotImplementedError("Implement this!")


class Chunk(IValid):
    def __init__(self, matrix):
        self.matrix = matrix
        self.matrix_size = len(matrix)
        self.list_of_numbers = range(1, self.matrix_size + 1)
        self.correct_sum = sum(self.list_of_numbers)
        self.correct_product = reduce(mul, self.list_of_numbers)

    def is_valid(self):
        for x in self.matrix:
            if not all(type(y) == type(int()) for y in x) or \
                    (sum(x) != self.correct_sum) or \
                    (reduce(mul, x) != self.correct_product):
                return False

        return True


class Row(Chunk):
    def __init__(self, matrix):
        Chunk.__init__(self, matrix)
        self.matrix = deepcopy(matrix)


class Col(Chunk):
    def __init__(self, matrix):
        Chunk.__init__(self, matrix)
        self.matrix = list(map(list, zip(*self.matrix)))


class Block(Chunk):
    def _divide_by_blocks(self):
        self.matrix = [x[i:i + self.step] for i in range(0, self.matrix_size, self.step) for x in self.matrix]
        return self

    def _demarcate_by_steps(self):
        self.matrix = [self.matrix[i:i + self.step] for i in range(0, len(self.matrix), self.step)]
        return self

    def _transpose_matrix(self):
        self.matrix = list(zip(*self.matrix))
        return self

    def _normalize(self):
        self.matrix = [list(chain(*y)) for x in self.matrix for y in x]
        return self

    def _blockToRow(self):
        self._divide_by_blocks() \
            ._demarcate_by_steps() \
            ._demarcate_by_steps() \
            ._transpose_matrix() \
            ._normalize()

    def __init__(self, matrix):
        Chunk.__init__(self, matrix)
        self.step = int(sqrt(self.matrix_size))
        self._blockToRow()


class Sudoku(IValid):
    def __init__(self, matrix):
        self.matrix = matrix
        self.block = Block(matrix)
        self.row = Row(matrix)
        self.col = Col(matrix)

    def is_valid(self):
        return self.row.is_valid() and \
               self.col.is_valid() and \
               self.block.is_valid()
