# -*- coding: utf-8 -*-
"""
ing1310-201520 02/09/2015 Ricardo Sat
"""



### Con while
nombreArchivo = raw_input("Ingrese el nombre del archivo:")  # se adjunta ejercicio2.txt
archivo = open(nombreArchivo)

linea = archivo.readline()
esDescendente = True

i = 0
while linea:
    lineaAnterior = linea
    linea = archivo.readline()
    if linea > lineaAnterior:
        esDescendente = False
        break

archivo.close()
print esDescendente



### Con for

nombreArchivo = raw_input("Ingrese el nombre del archivo:")  # se adjunta ejercicio2.txt
archivo = open(nombreArchivo)
esDescendente = True

i = 0
for linea in archivo:
    if i == 0:
        lineaAnterior = linea

    if linea > lineaAnterior:
        esDescendente = False
        break
    lineaAnterior = linea
    i += 1

archivo.close()
print esDescendente
