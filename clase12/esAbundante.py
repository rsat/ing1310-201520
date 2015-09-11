# -*- coding: utf-8 -*-
"""
ing1310-201520 11/09/2015 Ricardo Sat
"""


def divisor(n, i):
    # solo para validar valores de i válidos
    if i <= 0:
        return -1

    divisor = 1
    # índice del divisor en que vamos
    idxDivisor = 1
    while divisor < n:
        if n % divisor == 0:
            # si es un divisor y es el iésimo que pedía el usuario
            # lo retornamos
            if idxDivisor == i:
                return divisor
            idxDivisor += 1
        divisor += 1
    # si llegamos al final y no encontramos el iésimo que
    # pedía el usuario retornamos -1
    return -1


def esAbuntante(n):
    sumaDivisores = 0
    i = 1
    while True:
        # obtenemos el divisor iésimo
        div = divisor(n, i)
        # si es menos uno nos pasamos y terminamos
        if div == -1:
            break
        # es un divisor lo acumulamos
        sumaDivisores += div
        # si ya cumplimos la condición de número abundante
        # terminamos el método con resultado True
        if sumaDivisores > n:
            return True
        i += 1
    # Al haber sumado todos los divisores
    # podemos ver si no es abundante
    return sumaDivisores > n
    # también podría ser en vez de la línea anterior
    # if sumaDivisores > n:
    #    return True
    # else:
    #    return False
