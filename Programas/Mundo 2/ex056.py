from datetime import date

somaIdade = 0
mediaIdade = 0
maiorIdadeHomem = 0
nomeVelho = ''
totMulher20 = 0

for p in range(1, 5):

    print('-=-'*8)
    print(f'----- {p} Pessoa -----')
    print('-=-'*8)

    nome = input('Nome: ').strip()

    idade = int(input('Idade: '))
    somaIdade += idade

    sexo = (input('Sexo [M/F]: ')).upper().strip()

    if p == 1 and sexo in 'Mm':
        maiorIdadeHomem = idade
        nomeVelho = nome
    if sexo in 'Mm' and idade > maiorIdadeHomem:
        maiorIdadeHomem = idade
        nomeVelho = nome

    if sexo in 'Ff' and idade < 20:
        totMulher20 += 1


mediaIdade = somaIdade/4
print(f'A média de idade do grupo é: {mediaIdade}')
print(
    f'O homem mais velho do grupo tem {maiorIdadeHomem} anos e se chama {nomeVelho}')
print(f'Ao todo, são {totMulher20} mulheres menores de 20 anos')
