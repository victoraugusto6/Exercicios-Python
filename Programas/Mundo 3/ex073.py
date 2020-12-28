brasileirao = ('São Paulo', 'Atlético-MG', 'Flamengo', 'Internacional', 'Grêmio', 'Palmeiras', 'Fluminense', 'Santos', 'Corinthians',
               'Ceará', 'Atlético-GO', 'Athletico', 'Red Bull Bragantino', 'Fortaleza', 'Sport', 'Bahia', 'Vasco', 'Goiás', 'Botafogo', 'Coritiba',)

print(f'5 primeiros colocados da tabela: {brasileirao[:5]}\n')
print(f'Os 4 últimos colocados da tabela: {brasileirao[-4:]}\n')
print(f'Lista com times em ordem alfabética: {sorted(brasileirao)}\n')
print(f'Fortaleza está na posição: {brasileirao.index("Flamengo")+1}º')
