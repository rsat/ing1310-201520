# -*- coding: utf-8 -*-
"""
ing1310-201520 02/10/2015 Ricardo Sat
"""

M = [["*", "*", " "],
     [" ", "*", " "],
     [" ", " ", "*"]]


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


def contarAsteriscos(m):
    cuentaAsteriscos = []
    for i in range(len(m)):
        filasAsteriscos = []
        for j in range(len(m[0])):

            sumaAsteriscos = 0
            for x in range(i - 1, (i + 1) + 1):
                for y in range(j - 1, (j + 1) + 1):
                    if x >= 0 and x < len(m) and y >= 0 \
                            and y < len(m[0]) and m[x][y] == "*":
                        sumaAsteriscos += 1
            if m[i][j] == "*":
                sumaAsteriscos -= 1
            filasAsteriscos.append(sumaAsteriscos)
        cuentaAsteriscos.append(filasAsteriscos)
    return cuentaAsteriscos


imprimirMatriz(M)
imprimirMatriz(contarAsteriscos(M))
