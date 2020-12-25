from datetime import date

maior = 0
menor = 0
for c in range(1, 8):
    n = int(input(f'Digite seu ano de nascimento da pessoa {c}: '))
    print(f'Idade da pessoa {c}: {date.today().year-n}')
    if (date.today().year-n) >= 21:
        maior += 1
    else:
        menor += 1
print(f'\nPessoas iguais ou maiores de 18 anos: {maior}')
print(f'Pessoas menores de 18 anos: {menor}')
