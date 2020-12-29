jogador = {'nome': input('Nome do Jogador: '),
           'gols': [0],
           'total': 0}

partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
gols = list()

for c in range(0, partidas):
    jogador['gols'] = int(input(f'Quantos gols na partida {c}? '))
    gols.append(jogador['gols'])
jogador['gols'] = gols
jogador['total'] = sum(gols)
print('-='*30)
print(jogador)
print('-='*30)
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}')
print('-='*30)
print(f'O jogador {jogador["nome"]} jogou {len(jogador["gols"])} partidas')
for c in range(0, partidas):
    print(f'     => Na partida {c}, fez {gols[c]} gols.')
print(f'Foi um total de {jogador["total"]} gols.')
