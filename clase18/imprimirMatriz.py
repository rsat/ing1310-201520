# -*- coding: utf-8 -*-
"""
ing1310-201520 02/10/2015 Ricardo Sat
"""

M = [[1, 2, 3, 4, 5],
     [6, 7, 8, 9, 1],
     [1, 1, 1, 1, 1]]


def imprimirMatriz(m):
    print "*" * (2) * len(m[0]) + "*"
    for lista in m:
        linea = "|"
        for elemento in lista:
            linea += str(elemento) + " "
        linea = linea[:-1]
        linea += "|"
        print linea
    print "*" * (2) * len(m[0]) + "*"


imprimirMatriz(M)
