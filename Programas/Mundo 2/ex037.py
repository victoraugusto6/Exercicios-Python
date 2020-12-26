n = int(input('Digite um número inteiro qualquer: '))

e = int(input('\nDigite uma opção para converter:\n1 - Para Binário\n2 - Para Octal\n3 - Para Hexadecimal\n'))

if(e == 1):
    print(f'{n} em Binário é: {bin(n)[2:]}')
elif (e == 2):
    print(f'{n} em Octal é: {oct(n)[2:]}')
elif (e == 3):
    print(f'{n} em Hexadecimal é: {hex(n)[2:]}')
else:
    print('Opção inválida')
