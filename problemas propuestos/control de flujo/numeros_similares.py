# -*- coding: utf-8 -*-
"""
ing1310-201520 22/08/2015 Ricardo Sat

Realice un programa que le pida tres números enteros a un usuario e imprima en consola True
o False, dependiendo si los números son similares entre ellos. Sean a, b y divisor tres números enteros,
a y b serán similares si y sólo si, divisor divide a ambos o divisor no divide a ninguno de los dos.
Al final de su programa deberá preguntarle al usuario si desea comprobar si otros números son similares

Ejemplo:

Ingrese a: 10
Ingrese b: 5
Ingrese divisor: 2
False
Desea comprobar si otros números son similares(s/n)? s

Ingrese a: 10
Ingrese b: 15
Ingrese divisor: 5
True
Desea comprobar si otros números son similares(s/n)? ...
...
"""

opc = "s"
while opc == "s":
    a = int(raw_input("Ingrese a: "))
    b = int(raw_input("Ingrese b: "))
    divisor = int(raw_input("Ingrese divisor: "))
    if (a % divisor == 0 and b % divisor == 0) or (a % divisor != 0 and b % divisor != 0):
        print True
    else:
        print False
    opc = raw_input("Desea calcular si otro numero es similar(s/n)?")
print "Programa terminado"
