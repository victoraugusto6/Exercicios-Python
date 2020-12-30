def moeda(v=0, moeda='R$'):
    return(f'{moeda}{v:.2f}'.replace('.', ','))


def metade(v, parm):
    r = v/2
    if parm == True:
        return moeda(r)
    else:
        return r


def dobro(v, parm):
    r = v*2
    if parm == True:
        return moeda(r)
    else:
        return r


def aumentando(v, p, parm):
    r = v + (v*(p/100))
    if parm == True:
        return moeda(r)
    else:
        return r


def reduzindo(v, p, parm):
    r = v - (v*(p/100))
    if parm == True:
        return moeda(r)
    else:
        return r
