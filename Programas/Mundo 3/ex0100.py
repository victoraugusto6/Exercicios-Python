from random import randint


def sorteio():
    print('Sorteando 5 valores da lista: ', end='')
    for c in range(0, 5):
        numeros.append(randint(0, 10))
    print(numeros)


def somaPar():
    s = 0
    print(f'Somando os valores pares de {numeros} temos', end=' ')
    for c in numeros:
        if (c % 2) == 0:
            s += c
    print(s)


numeros = list()
sorteio()
somaPar()
