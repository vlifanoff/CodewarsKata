#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tic-Tac-Toe Checker: https://www.codewars.com/kata/525caa5c1bf619d28c000335"""


def isSolved(board):
    tmp = board + \
          list(zip(*board))[::-1] + \
          list(zip(*[[board[x][x], board[x][y]] for x, y in enumerate(range(len(board) - 1, -1, -1))]))

    for x in tmp:
        if x.count(1) == len(board) or x.count(2) == len(board):
            return x[0]

    return -1 if 0 in [tmp[i][j] for j in range(len(board)) for i in range(len(tmp))] else 0
