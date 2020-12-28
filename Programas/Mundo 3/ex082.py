e = 's'
v = []
vp = []
vi = []

while(e == 's'):
    v.append(int(input('Digite um número: ')))
    e = input('Deseja continuar? [S/N] ').lower()
    if(e == 'n'):
        for c in v:
            if(c % 2) == 0:
                vp.append(c)
            else:
                vi.append(c)
        print(f'\nLista original: {v}')
        print(f'Lista com valores pares: {vp}')
        print(f'Lista com valores ímpares: {vi}')
        break
