# Par ou Ímpar até perder, somando vitórias
from random import randint

v = 0

print(15*'-=-')
print('PAR OU ÍMPAR')
print(15*'-=-')

while True:

    jogador = int(input('\nDigite um valor: '))

    e = input('Escolha Par ou Ímpar. [P/I]: ').upper().strip()

    maquina = randint(0, 10)

    n = jogador+maquina

    print(
        f'Você jogou {jogador} e a máquina {maquina}. Somando deu {jogador+maquina}')
    if(e == 'P' and (n % 2) == 0):
        print('Você venceu! Vamos jogar novamente!')
        v += 1
    elif v == 1:
        print(f'Você perdeu com {v} vitória no total.')
        break
    else:
        print(f'Você perdeu com {v} vitórias no total.')
        break
