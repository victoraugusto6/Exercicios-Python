salario = float(input('Digite seu salário: '))

if(salario > 1250):
    print(
        f'Seu salário de R${salario} subirá para R${salario+(salario*(10/100))}')
else:
    print(
        f'Seu salário de R${salario} subirá para R${salario+(salario*(15/100))}')
