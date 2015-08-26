# -*- coding: utf-8 -*-
"""
ing1310-201520 26/08/2015 Ricardo Sat
Programa que recibe dos números enteros, a y b, y imprime el resultado de a^b o a**b.
No se puede utilizar el operador ** y acepta cualquier número entero
"""

a = int(raw_input("Ingrese a: "))
b = int(raw_input("Ingrese b: "))

# contando hacia adelante
suma = 1
i = 0
while i < abs(b):
    suma *= a
    i += 1
if (b < 0):
    print 1.0 / suma
else:
    print suma

a = int(raw_input("Ingrese a: "))
b = int(raw_input("Ingrese b: "))

# contando hacia atras
suma = 1
tieneExponenteNegativo = b < 0
while abs(b) > 0:
    suma *= a
    b = abs(b) - 1
if tieneExponenteNegativo:
    print 1.0 / suma
else:
    print suma
