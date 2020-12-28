print('-'*40)
print(f'{"LISTAGEM DE PREÇOS":^40}')
print('-'*40)

tupla = ('Lápis', 1.75, 'Borracha', 2, 'Caderno', 15.90)

for c in range(0, len(tupla), 2):
    print(f'{tupla[c]:.<30}', end='')
    print(f'R$ {tupla[c+1]:>7.2f}')

print('-'*40)
