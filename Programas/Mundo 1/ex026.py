n = input('Digite seu nome: ').lower().strip()
qtdLetraA = n.count('a')
primeiraPosA = n.find('a')
ultimaPosA = n.rfind('a')

print(f'Aparece a letra A: {qtdLetraA} vezes')
print(f'Aparece a letra A primeiro na posição: {primeiraPosA}')
print(f'Aparece a letra a na última posição em: {ultimaPosA}')
