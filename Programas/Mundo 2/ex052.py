n = int(input('Digite um número: '))
tot = 0

for c in range(1, n+1):
    if(n % c) == 0:
        print('\033[33m', end=' ')
        tot += 1
    else:
        print('\033[031m', end=' ')
    print('{}'.format(c), end=' ')
print(f'\033[m\nO número {n} foi divisível {tot} vezes.')
if(tot == 2):
    print(f'Portanto, {n} é um número primo')
else:
    print(f'Portanto, {n} NÃO é um número primo')
