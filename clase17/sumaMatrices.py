# -*- coding: utf-8 -*-
"""
ing1310-201520 30/09/2015 Ricardo Sat
"""


# las siguientes dos funciones suman las columnas impares de la matriz o lista de listas
# estas lo hacen recorriendo fila por fila y sumando las posiciones impares

def sumaColumnasImpares(M):
    suma = 0
    for fila in M:
        for i in range(1, len(fila), 2):
            suma += fila[i]
    return suma


def sumaColumnasImpares2(M):
    suma = 0
    for i in range(len(M)):
        for j in range(len(M[i])):
            if j % 2 != 0:
                suma += M[i][j]
    return suma


# las siguiente función suman las columnas impares de la matriz o lista de listas
# esta lo hace recorriendo columna por columna siempre y cuando tenga índice impar

def sumaColumnasImpares3(M):
    suma = 0
    for j in range(len(M[0])):  # esto es válido ya que se supone que la matriz es rectangular
        for i in range(len(M)):
            if j % 2 != 0:
                suma += M[i][j]
    return suma


M = [[1, 2, 3, 4, 5],
     [6, 7, 8, 9, 10],
     [11, 12, 13, 14, 15]]

print sumaColumnasImpares(M)
print sumaColumnasImpares(M) == sumaColumnasImpares2(M) == sumaColumnasImpares3(M)
