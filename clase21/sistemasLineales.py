# -*- coding: utf-8 -*-
"""
ing1310-201520 14/10/2015 Ricardo Sat
"""

# parte 1
from numpy import random

n = -1
while n < 0:
    n = int(raw_input('Ingrese la cantidad de ecuaciones: '))

archivo = open('sistemaLineal.txt', 'w')
# escribir n
archivo.write(str(n) + '\n')

# escribir la matriz
for fila in range(n):
    for numero in range(n):
        archivo.write(str(random.randint(-100, 100) + random.random()) + ' ')
    archivo.write('\n')

# escribir b
for fila in range(n):
    archivo.write(str(random.randint(-100, 100) + random.random()) + '\n')

archivo.close()
