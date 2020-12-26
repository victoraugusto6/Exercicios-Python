from random import randint

print('Tente acertar um número entre 0 e 10!\n')

maquina = randint(0, 10)
jogador = -1

while(jogador is not maquina):
    jogador = int(input('Escolha um número: '))
    print(f'Você escolheu {jogador} e a máquina {maquina}')

if(jogador == maquina):
    print('Parabéns! Você acertou')
