dados = dict()
pessoas = list()
mulheres = list()
somaIdades = mediaIdades = 0
while True:
    dados['nome'] = input('Nome: ')
    dados['sexo'] = input('Sexo [M/F]: ').lower()

    while dados['sexo'] not in 'mf':
        dados['sexo'] = input('Sexo [M/F]: ')
    dados['idade'] = int(input('Idade: '))
    pessoas.append(dados.copy())

    if dados['sexo'] == 'f':
        mulheres.append(dados.copy())

    dados.clear()

    e = input('Deseja continuar? [S/N] ')
    if e == 'n':
        break
print()
print('-='*20)
print(f'Foram cadastradas {len(pessoas)} pessoas')

for p in pessoas:
    for k, v in p.items():
        if k == 'idade':
            somaIdades += v
mediaIdades = somaIdades/len(pessoas)
print(f'A média de idade é: {mediaIdades:.2f}')

print(f'Lista com as mulheres da lista: ', end='')
for p in mulheres:
    for k, v in p.items():
        if k == 'nome':
            print(f'{v} -', end=' ')
print()

print('Lista de pessoas com idade acima da média: ')
for p in pessoas:
    for k, v in p.items():
        if k == 'idade' and v > mediaIdades:
            for k, v in p.items():
                print(f' {k} = {v}', end='; ')
print('\n<< ENCERRADO >>')
print()
