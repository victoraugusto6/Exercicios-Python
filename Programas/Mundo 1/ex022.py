nome = input('Nome completo: ')

print(f'Nome com letras maísculas: {nome.upper()}')

print(f'Nome com letras minísculas: {nome.lower()}')

nomeSemEspaço = nome.replace(' ', '')
print(f'Quantas letras, sem considerar espaço: {len(nomeSemEspaço)}')

nomeSeparado = nome.split()
print(f'O primeiro nome tem: {len(nomeSeparado[0])} letras')