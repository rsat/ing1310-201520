def divisores(num):
    i = 1
    lista = []
    while i <= num:
        if num % i == 0:
            lista.append(i)
        i += 1
    return lista


def divisoresDistintos(lista):
    divisoresUnicos = []
    for numero in lista:
        divisoresActual = divisores(numero)
        for divisor in divisoresActual:
            if divisor not in divisoresUnicos:
                divisoresUnicos.append(divisor)
    divisoresUnicos.sort()
    return divisoresUnicos


print divisoresDistintos([1, 2, 3, 6, 7, 8])
