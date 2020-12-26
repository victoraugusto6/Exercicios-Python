km = float(input('Quantidade de Km rodados: '))
dias = int(input('Quantidade de dias alugados: '))

preco = (60*dias) + (0.15*km)

print(f'Valor a pagar: {preco:.2f}')