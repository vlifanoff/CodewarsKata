#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Decode the Morse code: https://www.codewars.com/kata/54b724efac3d5402db00065e"""

import re

chart_morse = {
    '-----': '0', '.----': '1', '..---': '2', '...--': '3', '....-': '4', '.....': '5', '-....': '6', '--...': '7',
    '---..': '8', '----.': '9', '.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D', '.': 'E', '..-.': 'F', '--.': 'G',
    '....': 'H', '..': 'I', '.---': 'J', '-.-': 'K', '.-..': 'L', '--': 'M', '-.': 'N', '---': 'O', '.--.': 'P',
    '--.-': 'Q', '.-.': 'R', '...': 'S', '-': 'T', '..-': 'U', '...-': 'V', '.--': 'W', '-..-': 'X', '-.--': 'Y',
    '--..': 'Z', '...---...': 'SOS', '.-.-.-': '.', '--..--': ',', '..--..': '?', '.----.': "'", '-.-.--': '!',
    '-..-.': '/', '-.--.': '(', '-.--.-': ')', '.-...': '&', '---...': ':', '-.-.-.': ';', '-...-': '=',
    '.-.-.': '+', '-....-': '-', '..--.-': '_', '.-..-.': '"', '...-..-': '$', '.--.-.': '@', '   ': ' ',
}


def decodeMorse(morseCode):
    return ''.join([chart_morse[x] for x in re.findall(r'[\.-]+|\s{3}', morseCode.strip())])


def decodeMorse2(morseCode):
    """The Morse code table is preloaded as a dictionary MORSE_CODE."""
    return ''.join([' ' if ' ' in x else MORSE_CODE[x] for x in re.findall(r'[\.-]+|\s{3}', morseCode.strip())])
