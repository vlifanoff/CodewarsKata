#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Welcome!: https://www.codewars.com/kata/577ff15ad648a14b780000e7"""

base_lang = {
    'english': 'Welcome',
    'czech': 'Vitejte',
    'danish': 'Velkomst',
    'dutch': 'Welkom',
    'estonian': 'Tere tulemast',
    'finnish': 'Tervetuloa',
    'flemish': 'Welgekomen',
    'french': 'Bienvenue',
    'german': 'Willkommen',
    'irish': 'Failte',
    'italian': 'Benvenuto',
    'latvian': 'Gaidits',
    'lithuanian': 'Laukiamas',
    'polish': 'Witamy',
    'spanish': 'Bienvenido',
    'swedish': 'Valkommen',
    'welsh': 'Croeso'
}


def greet(language):
    try:
        return base_lang[language]
    except KeyError:
        return base_lang['english']
