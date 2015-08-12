# -*- coding: utf-8 -*-
"""
ing1310-201520 12/08/2015 Ricardo Sat

Programa que resuelve ecuación cuadrática de la forma a*x^2 + b*x + c

Si es que la raíz es compleja el programa terminará con el error
ValueError: math domain error

"""
# importamos el módulo math para calcular la raíz cuadrada
import math

# Solicitamos los valores de los coeficientes a los usuarios
a = raw_input("Ingrese coeficiente a:")
b = raw_input("Ingrese coeficiente b:")
c = raw_input("Ingrese coeficiente c:")

# Transformamos las variables de string-texto- a float-decimal-
a = float(a)
b = float(b)
c = float(c)

# calculamos las raíces según la fórmula cuadrática
x1 = (-b + math.sqrt(b*b - 4*a*c))/2*a
x2 = (-b - math.sqrt(b*b - 4*a*c))/2*a

# imprimimos los resultados
print "X1:", x1, "X2:", x2
