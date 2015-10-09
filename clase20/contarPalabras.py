# -*- coding: utf-8 -*-
"""
ing1310-201520 09/10/2015 Ricardo Sat
"""


def contarPalabra(s):
    palabras = s.split()
    indicePalabras = {}
    for palabra in palabras:
        if palabra not in indicePalabras:
            indicePalabras[palabra] = 1
        else:
            indicePalabras[palabra] += 1
    return indicePalabras


print contarPalabra("el curso de introduccion a la computacion tiene muchas evaluaciones en el curso")


def transformarATupla(s):
    listaTuplas = []
    indicePalabras = contarPalabra(s)
    for palabra, frecuencia in indicePalabras.items():
        if len(palabra) > 3:
            nuevaTupla = palabra, frecuencia
            listaTuplas.append(nuevaTupla)
    return listaTuplas


print transformarATupla("el curso de introduccion a la computacion tiene muchas evaluaciones en el curso")

ventaDiarias = [('US', 50), ('L', 200), ('EUR', 300),
                ('L', 100), ('CH', 21000), ('US', 150),
                ('EUR', 100)]


def ventaDiaria(ventaDiarias):
    monedas = {}
    for venta in ventaDiarias:
        moneda, cantidad = venta
        #        moneda = venta[0]
        #        cantidad = venta[1]
        if moneda not in monedas:
            monedas[moneda] = cantidad
        else:
            monedas[moneda] += cantidad
    return monedas


print ventaDiaria(ventaDiarias)

monedas = {'US': ('Dolares', 500),
           'EUR': ('Euros', 600),
           'L': ('Libras', 700),
           'CH': ('Pesos Chilenos', 1)}


def totalVentaDiaria(monedas, ventasDiarias):
    totalVentas = ventaDiaria(ventaDiarias)
    suma = 0
    for moneda, totalMoneda in totalVentas.items():
        suma += totalMoneda * monedas[moneda][1]
    return suma


def totalVentaDiaria2(monedas, ventasDiarias):
    totalVentas = ventaDiaria(ventaDiarias)
    suma = []
    for moneda, totalMoneda in totalVentas.items():
        suma.append(totalMoneda * monedas[moneda][1])
    return suma


print totalVentaDiaria(monedas, ventaDiarias)


def totalVentaDiaria(monedas, ventasDiarias):
    totalVentas = ventaDiaria(ventaDiarias)
    suma = 0
    for moneda in totalVentas:
        suma += totalVentas[moneda] * monedas[moneda][1]
    return suma


print totalVentaDiaria(monedas, ventaDiarias)


def convertir(monedas, ventasDiarias, moneda):
    ventaEnMoneda = []
    ventasEnPesos = totalVentaDiaria2(monedas, ventaDiarias)
    for venta in ventasEnPesos:
        ventaEnMoneda.append(venta / monedas[moneda][1])
    print ventaEnMoneda


convertir(monedas, ventaDiarias, "US")
