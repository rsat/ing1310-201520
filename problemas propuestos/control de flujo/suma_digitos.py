# -*- coding: utf-8 -*-
"""
ing1310-201520 22/08/2015 Ricardo Sat

Realice un programa que reciba un número entero e imprima en consola la suma de sus dígitos. Al final de su
programa deberá preguntarle al usuario si quiere calcular la suma de los dígitos de otro número.

Ejemplo

Ingrese un número: 111
La suma de los dígitos de 111 es 3
Desea calcular la suma de los dígitos de otro número(s/n)? s
Ingrese un número: 942
La suma de los dígitos de 942 es 15
Desea calcular la suma de los dígitos de otro número(s/n)? ...
...
"""

opc = "s"
while opc == "s":
    sumaDigitos = 0
    n = int(raw_input("Ingrese un numero: "))
    numeroOriginal = n
    while n > 0:
        sumaDigitos += n % 10
        n /= 10
    print "La suma de los digitos de", numeroOriginal, "es", sumaDigitos
    opc = raw_input("Desea calcular la suma de los digitos de otro numero(s/n)?")
