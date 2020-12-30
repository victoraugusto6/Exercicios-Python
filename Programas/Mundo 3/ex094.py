pessoas = list()
pessoa = dict()
somaIdades = mediaIdades = 0

while True:
    pessoa.clear()
    pessoa['nome'] = input('Nome: ')
    while True:
        pessoa['sexo'] = input('Sexo [M/F]: ').upper()[0]
        if pessoa['sexo'] in 'MF':
            break
        print('ERRO! Por favor, digite apenas M ou F.')
    pessoa['idade'] = int(input('Idade: '))
    somaIdades += pessoa['idade']
    pessoas.append(pessoa.copy())
    while True:
        e = input('Deseja continuar? [S/N] ').upper()[0]
        if e in 'SN':
            break
        print('ERRO! Responda apenas S ou N. ')
    if e == 'N':
        break
print('-='*40)
print(f'A) Ao todo temos {len(pessoas)} pessoas cadastradas.')
mediaIdades = somaIdades/len(pessoas)
print(f'B) A média de idade é de {mediaIdades:5.2f} anos.')
print(f'C) As mulheres cadastras foram: ', end='')
for p in pessoas:
    if p['sexo'] in 'F':
        print(f'{p["nome"]}', end=' ')
print()
print('D) As pessoas com idade acima da média foram: ')
for p in pessoas:
    if p['idade'] >= mediaIdades:
        print(
            f'Nome: {p["nome"]}; Sexo: {p["sexo"]}; Idade: {p["idade"]}')
print('<< ENCERRADO >>')
