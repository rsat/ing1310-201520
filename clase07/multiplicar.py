# -*- coding: utf-8 -*-
"""
ing1310-201520 26/08/2015 Ricardo Sat
Programa que recibe dos números enteros, a y b, y imprime el resultado de a*b.
No se puede utilizar el operador *

"""


##### Las soluciones desde aqui hasta nuevo aviso, suponen que a >= 0 #####
print "Ingrese valores > 0 para a"
# Sol 1
print "Sol 1"
a = int(raw_input("Ingrese a: "))
b = int(raw_input("Ingrese b: "))

suma = 0
i = 0
while i < a:
    suma += b
    i += 1
print suma

# Sol 2
print "Sol 2"
a = int(raw_input("Ingrese a: "))
b = int(raw_input("Ingrese b: "))

# contamos hacia abajo(la variable a va decreciendo) y nos ahorramos una variable (i)
suma = 0
while a > 0:
    suma += b
    a -= 1
print suma


##### Las soluciones desde aqui hasta arriba suponen que a >= 0 #####
print "Ahora a puede tomar valores negativos"

##### Las soluciones desde aqui hasta abajo funcionan para todos los casos #####

# Sol 1.1
print "Sol 1.1"
a = int(raw_input("Ingrese a: "))
b = int(raw_input("Ingrese b: "))

suma = 0
i = 0
while i < abs(a):
    suma += b
    i += 1

if a < 0:
    print -suma
else:
    print suma


# Sol 2.1
print "Sol 2.1"
a = int(raw_input("Ingrese a: "))
b = int(raw_input("Ingrese b: "))

suma = 0
esPrimerOperandoNegativo = a < 0
while abs(a) > 0:
    suma += b
    a = abs(a) - 1
if esPrimerOperandoNegativo:
    print -suma
else:
    print suma

# Sol 3 otra solución más, nada especial
print "Sol 3"
a = int(raw_input("Ingrese a: "))
b = int(raw_input("Ingrese b: "))

suma = 0
i = 0
while i < abs(a):
    suma += abs(b)
    i += 1

if (a < 0 and b > 0) or (a > 0 and b < 0):  # si a o b es igual a 0, la suma será 0
    suma = -suma

print suma
