n1 = int(input('Digite um valor: '))
n2 = int(input('Digite um valor: '))
n3 = int(input('Digite um valor: '))
n4 = int(input('Digite um valor: '))

tupla = (n1, n2, n3, n4)
v9 = 0

for c in range(0, len(tupla)):
    if(tupla[c] == 9):
        v9 += 1

print(f'Você digitou os valores: {tupla}')
print(f'O valor 9 apareceu {v9} vezes')
if(tupla.count(3) > 0):
    print(f'O valor 3 apareceu na {tupla.index(3)+1}º posição')
else:
    print('O valor 3 apareceu em nenhuma posição')
print(f'Os valores pares são: ', end=' ')
for c in range(0, len(tupla)):
    if(tupla[c] % 2) == 0:
        print(tupla[c], end=' ')
print('')
