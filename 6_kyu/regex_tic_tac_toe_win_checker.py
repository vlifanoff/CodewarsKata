#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Regex Tic Tac Toe Win Checker: https://www.codewars.com/kata/582e0450fe38013dbc0002d3"""


def regex_tic_tac_toe_win_checker(board):
    sp_brd = [board[0:3], board[3:6], board[6:9]]
    tmp = sp_brd + \
          list(map(''.join, zip(*sp_brd)))[::-1] + \
          list(map(''.join, zip(*[[sp_brd[x][x], sp_brd[x][y]] for x, y in enumerate(range(2, -1, -1))])))

    for x in tmp:
        if x == 'XXX' or x == 'OOO':
            return True

    return False
