def leiaInt(msg):
    while True:
        try:
            a = int(input(msg))
        except (ValueError, TypeError):
            print('\033[31mERRO! Digite um número inteiro válido.\033[m')
            continue
        else:
            return int(a)


def leiaFloat(msg):
    while True:
        try:
            a = float(input(msg))
        except (ValueError, TypeError):
            print('\033[31mERRO! Digite um número inteiro válido.\033[m')
            continue
        except (KeyboardInterrupt):
            print('\033[31mEntrada de dados interrompida pelo usuário.\033[m')
            return 0
        else:
            return float(a)


n = leiaInt('Digite um número: ')
print(f'Você acabou de digitar o número {n}')
