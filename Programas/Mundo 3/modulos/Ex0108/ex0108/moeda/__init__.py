def metade(v):
    r = v/2
    return r


def dobro(v):
    r = v*2
    return r


def aumentando(v, p):
    n = v + (v*(p/100))
    return n


def reduzindo(v, p):
    n = v - (v*(p/100))
    return n


def moeda(v=0, moeda='R$'):
    return(f'{moeda}{v:.2f}'.replace('.', ','))
