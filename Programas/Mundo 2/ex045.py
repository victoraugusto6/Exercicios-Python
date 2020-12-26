from random import randint

itens = ['Pedra', 'Papel', 'Tesoura']

jogador = int(input('''Escolha entre:
0 - Pedra
1 - Papel
2 - Tesoura\n\n'''))

maquina = randint(0, 2)

print('-='*11)
print(f'Você jogou {itens[jogador]}\nA máquina escolheu {itens[maquina]}')
print('-='*11)

if(jogador == 0 and maquina == 2):
    print('Você ganhou! Pedra ganha de tesoura')
elif (jogador == 1 and maquina == 0):
    print('Você ganhou! Papel ganha de pedra')
elif (jogador == 2 and maquina == 1):
    print('Você ganhou! Tesoura ganha de papel')
elif jogador == maquina:
    print('Empate')
else:
    print('Você perdeu')
