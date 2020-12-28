exp = str(input('Digite a expressão: '))
cont = 0

for x in exp:
    if x == '(':
        cont += 1
    elif x == ')':
        cont -= 1
        if cont < 0:  # Fechou antes de abrir
            print('Expressao inválida')
            exit(0)  # Termina programa

if cont != 0:  # Tem parênteses sem seu par
    print('Expressao inválida')
else:
    print('Expressao válida')
