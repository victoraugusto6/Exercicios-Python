jogador = dict()
gols = list()
jogadores = list()

while True:
    jogador.clear()
    gols.clear()
    jogador['nome'] = input('Nome do jogador: ')
    partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    for g in range(0, partidas):
        gols.append(int(input(f' -> Quantos gols na partida {g+1}: ')))

    jogador['gols'] = gols[:]
    jogador['total'] = sum(gols)
    jogadores.append(jogador.copy())

    while True:
        e = input('Deseja continuar? [S/N] ').upper()[0]
        if e in 'SN':
            break
        print('ERRO! Responda apenas S ou N.')
    if e == 'N':
        break
print('-='*40)
print(f'{"cod":<4}{"nome":<10}{"gols":<20}{"total"}')
print('-'*40)
for i, p in enumerate(jogadores):
    print(f'{i:<4}{p["nome"]:<10}{p["gols"]}{p["total"]:>20}')
print('-'*40)
while True:
    e = int(input('Mostrar dados de qual jogador? (999 para interromper) '))
    if(e == 999):
        break
    print(f'LEVANTAMENTO DO JOGADOR {jogadores[e]["nome"]}')
    for i, p in enumerate(jogadores):
        for c in range(0, len(p['gols'])):
            if i == e:
                print(f'    No jogo {c+1} fez {p["gols"][c]} gols')
    print('-'*40)
