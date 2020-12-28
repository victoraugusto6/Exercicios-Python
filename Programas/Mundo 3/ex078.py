num = []

for v in range(0, 5):
    num.append(int(input(f'Digite um valor na posição {v}: ')))

print(f'\nValores: {num}')

print(f'O menor valor foi: {min(num)} na posição ', end='')
for v in range(0, len(num)):
    if num[v] == min(num):
        print(v, end=' ')

print(f'\nO maior valor foi: {max(num)} na posição ', end='')
for v in range(0, len(num)):
    if num[v] == max(num):
        print(v, end=' ')

print()
