valores = []
e = 's'
while e == 's':
    valores.append(int(input('Digite um valor: ')))
    if(valores[-1] in valores[:-1]):
        print('Valor duplicado.')
        valores.pop()
    else:
        print('Valor adicionado com sucesso!')
    e = input('Deseja continuar? [S/N] ')
    if(e == 'n'):
        valores.sort()
        print(valores)
        break
