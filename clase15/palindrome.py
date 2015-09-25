# -*- coding: utf-8 -*-
"""
ing1310-201520 25/09/2015 Ricardo Sat
"""

# -*- coding: utf-8 -*-
"""
ing1310-201520 25/09/2015 Ricardo Sat
"""


def esPalindroma(s):
    return s == s[::-1]


def esPalindroma2(x):
    i = 0
    j = len(x) - 1
    while i < j:
        if x[i] != x[j]:
            return False
        i += 1
        j -= 1
    return True


def esPalindroma3(x):
    lista = list(x)
    lista.reverse()
    return lista == list(x)


def esPalindroma4(x):
    stringComoLista = list(x)
    listaInvertida = stringComoLista[:]
    listaInvertida.reverse()
    return stringComoLista == listaInvertida
