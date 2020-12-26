n1 = float(input('Primeiro número: '))
n2 = float(input('Segundo número: '))
e = 0
while(e is not 5):
    e = int(input('''Escolha:
    [ 1 ] - Somar
    [ 2 ] - Multiplicar
    [ 3 ] - Maior
    [ 4 ] - Novos números
    [ 5 ] - Sair
    >>>Qual sua opção?\n'''))

    if(e == 1):
        print(f'A soma entre {n1} e {n2} é: {n1+n2}')
    elif(e == 2):
        print(f'A multiplicação entre {n1} e {n2} é: {n1*n2}')
    elif(e == 3):
        if(n1 > n2):
            print(f'O maior número entre {n1} e {n2} é: {n1}')
        elif(n1 < n2):
            print(f'O maior número entre {n1} e {n2} é: {n2}')
        else:
            print(f'{n1} e {n2} são iguais')
    if(e == 4):
        n1 = float(input('Primeiro número: '))
        n2 = float(input('Segundo número: '))
