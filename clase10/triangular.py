# -*- coding: utf-8 -*-
"""
ing1310-201520 04/09/2015 Ricardo Sat

Programa que lee el archivo "numeros.txt con números e imprime en
"salida.txt" si los números son triángulares
"""

numeros = open("numeros.txt")
salida = open("salida.txt", "w")

for numero in numeros:
    numeroBuscado = int(numero)
    n = 1
    m = 0
    while m < numeroBuscado:
        m = n * (n + 1) / 2
        n += 1

    if numeroBuscado == m:
        salida.write(str(numeroBuscado) + " es triangular\n")
    else:
        salida.write(str(numeroBuscado) + " no es triangular\n")
