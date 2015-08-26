# -*- coding: utf-8 -*-
"""
ing1310-201520 26/08/2015 Ricardo Sat
Programa que pide que se ingresen temperaturas hasta que el usuario
ingresa ".". Luego imprime la temperatura máxima, mínima ingresada
y el promedio de todas.
"""

tIngresada = ""
suma = 0
i = 0
tempMin = 0
tempMax = 0
while True:
    tIngresada = raw_input("Ingrese una temperatura(. para terminar): ")

    if tIngresada == ".":
        break

    t = float(tIngresada)

    if i == 0:
        tempMax = t
        tempMin = t

    if t < tempMin:
        tempMin = t
    if t > tempMax:
        tempMax = t

    suma += t
    i += 1

if i > 0:
    print "El promedio es", suma / i
    print "La temperatura mínima es", tempMin
    print "La temperatura máxima es", tempMax
else:
    print "No se ingresaron temperaturas"
