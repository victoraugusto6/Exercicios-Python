lista = list()

for c in range(0, 7):
    lista.append(int(input(f'Digite um valor na posição {c}º: ')))

lista.sort()

print('Os valores pares da lista foram: ', end='')
for c in lista:
    if(c % 2) == 0:
        print(f'{c}', end=' ')

print('\nOs valores ímpares da lista foram: ', end='')
for c in lista:
    if(c % 2) != 0:
        print(f'{c}', end=' ')
print()
