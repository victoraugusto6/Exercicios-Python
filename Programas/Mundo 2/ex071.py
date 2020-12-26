# Banco
ced50 = ced20 = ced10 = ced1 = 0

valor = int(input('Qual valor deseja sacar? '))
resto = 0

if valor > 50:
    while valor >= 50:
        valor -= 50
        ced50 += 1
    while valor >= 20:
        valor -= 20
        ced20 += 1
    while valor >= 10:
        valor -= 10
        ced10 += 1
    while valor >= 1:
        valor -= 1
        ced1 += 1

if(ced50 > 0):
    print(f'\nTotal de {ced50} cédulas de R$50,00')
if(ced20 > 0):
    print(f'Total de {ced20} cédulas de R$20')
if(ced10 > 0):
    print(f'Total de {ced10} cédulas de R$10')
if(ced1 > 0):
    print(f'Total de {ced1} cédulas de R$1')
