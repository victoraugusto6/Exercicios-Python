def leiaInt(msg):
    while True:
        a = input(msg)
        if a.isnumeric():
            return int(a)
            break
        else:
            print('\033[31mERRO! Digite um número inteiro válido.\033[m')


n = leiaInt('Digite um número: ')
print(f'Você acabou de digitar o número {n}')
