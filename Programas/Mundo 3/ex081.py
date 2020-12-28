v = []
e = 's'
while e == 's':
    v.append(int(input('Digite um número: ')))
    e = input('Deseja continuar? [S/N] ').lower()
    if(e == 'n'):
        print('-=-'*10)
        print(f'Foram digitados {len(v)} números')
        v.sort(reverse=True)
        print(f'Lista de valores ordenadas de forma decrescente: {v}')
        if 5 in v:
            print('Foi encontrado o valor 5')
        else:
            print('Não foi encontrado o valor 5')
        break
