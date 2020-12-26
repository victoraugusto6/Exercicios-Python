pesos = []

for c in range(1, 7):
    n = float(input(f'Digite o peso da pessoa {c}: '))
    pesos.append(n)

print(f'O menor peso foi: {min(pesos)}\nO maior peso foi: {max(pesos)}')
