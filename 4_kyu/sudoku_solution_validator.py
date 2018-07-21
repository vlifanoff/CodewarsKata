#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Sudoku Solution Validator: https://www.codewars.com/kata/529bf0e9bdf7657179000008"""

BOARD_LENGTH = 9
BOARD_TUPLE_LENGTH = 3
BOARD_TUPLE_STEP = BOARD_TUPLE_LENGTH


def boardArrayToTuple(board):
    board_triple = []

    for brd in board:
        board_tmp = [None for _ in range(BOARD_TUPLE_LENGTH)]

        for i in range(0, len(brd), BOARD_TUPLE_STEP):
            board_tmp[i / BOARD_TUPLE_LENGTH] = (brd[i], brd[i + 1], brd[i + 2])

        board_triple.append(board_tmp)

    return board_triple


def boardTranspose(board):
    board_t = []

    for i in range(0, len(board), BOARD_TUPLE_STEP):
        for x in map(list, zip(board[i], board[i + 1], board[i + 2])):
            board_t.append(x)

    return board_t


def boardTupleToArray(board):
    result = []

    for x in board:
        tmp = []
        for y in x:
            for z in y:
                tmp.append(z)
        result.append(tmp)

    return result


def blockToRow(board):
    return boardTupleToArray(boardTranspose(boardArrayToTuple(board)))


def validBoardLength(board):
    if len(board) != BOARD_LENGTH:
        return False

    for i in board:
        if len(board) != BOARD_LENGTH:
            return False

    return True


def validNumbers(board):
    for x in board:
        num = {x + 1: True for x in range(BOARD_LENGTH)}
        for y in x:
            if y == 0: continue
            if y in num:
                del num[y]
            else:
                return False

    return True


def validSolution(board):
    if validBoardLength(board) \
            and validNumbers(board) \
            and validNumbers(map(list, zip(*board))) \
            and validNumbers(blockToRow(board)):
        return True

    return False
