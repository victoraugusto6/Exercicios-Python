def resumo(v, aum=10, red=5):
    print('-'*30)
    print('RESUMO DE VALOR'.center(30))
    print('-'*30)

    print(f'Preço analisado:     {moeda(v)}')
    print(f'Dobro do preço:      {(dobro(v)):}')
    print(f'Metade do preço:     {(metade(v))}')
    print(f'{aum}% de aumento:      {(aumentando(v,aum))}')
    print(f'{red}% de redução:      {(reduzindo(v,red))}')
    print('-'*30)


def moeda(v=0, moeda='R$'):
    return f'{moeda}{v:>.2f}'.replace('.', ',')


def metade(v, parm=True):
    r = v/2
    if parm == True:
        return moeda(r)
    else:
        return r


def dobro(v, parm=True):
    r = v*2
    if parm == True:
        return moeda(r)
    else:
        return r


def aumentando(v, p, parm=True):
    r = v + (v*(p/100))
    if parm == True:
        return moeda(r)
    else:
        return r


def reduzindo(v, p, parm=True):
    r = v - (v*(p/100))
    if parm == True:
        return moeda(r)
    else:
        return r
