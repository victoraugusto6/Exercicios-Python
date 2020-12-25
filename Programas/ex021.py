from random import randint
from time import sleep

# Aleatório de 0 a 5
r = randint(0, 5)

print('-+-'*20)

print('Escolha um número e tente acertar!')

print('-+-'*20)

n = int(input('Digite um número: '))

print('Pensando...')

sleep(3)

if (r == n):
    print(f'Você acertou! O valor escolhido foi {r}')
else:
    print('Você errou, o valor escolhido foi {}'.format(r))
