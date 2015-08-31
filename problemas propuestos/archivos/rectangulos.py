# -*- coding: utf-8 -*-
"""
ing1310-201520 30/08/2015 Ricardo Sat

Realice un programa que lea el archivo rectangulos.txt, el cual tiene la siguiente estructura:

1era línea: un número entero positivo que representa la cantidad de rectángulos que describe el archivo
2da  línea: posición x del primer rectángulo
3era línea: posición y del primer rectángulo
4ta  línea: ancho del primer rectángulo
5ta  línea: alto del primer rectángulo
6ta  línea: posición x del segundo rectángulo
7ma  línea: posición y del segundo rectángulo
8va  línea: ancho del segundo rectángulo
9na  línea: alto del segundo rectángulo
... etc

Un rectángulo está descrito de esta forma:

x0, y0 ****************
*                     *
*                     *
*                     *
*                     *
***********************

Donde x0, y0 es la posición del rectángulo que se da
Los asteriscos en vertical representan la altura del rectángulo
Los asteriscos en horizontal representan el ancho del rectángulo


Archivo de ejemplo de rectangulos.txt:
3
3.5
4
4
4
2
2
3
4
-7
-2
4
2

Arriba en el archivo se describen 3 rectángulos
con coordenadas 3.5, 4 y ancho 4 y largo 4
con coordenadas 2, 2 y ancho 3 y largo 4
con coordenadas -7, -2 y ancho 4 y largo 2

Su programa deberá generar un archivo resultados.txt donde en su interior deberá contener en cada línea True o False
dependiendo si el primer rectángulo que aparece en el archivo rectangulos.txt se intersecta con los rectángulos restantes

En la primera línea del archivo resultados.txt se encontrará el valor para el primer rectángulo y el segundo, luego en
la segunda línea el valor para el primer rectángulo y el tercero, y así sucesivamente.

Si su programa toma el archivo rectangulos.txt de ejemplo debería generar el archivo resultados.txt con lo siguiente:
True
False

"""
