matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
vPares = terColuna = maiorSegLinha = 0

for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para [{l},{c}]: '))
print('-='*15)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
        if matriz[l][c] % 2 == 0:
            vPares += matriz[l][c]
        if c == 2:
            terColuna += matriz[l][c]
        if l == 1:
            if matriz[l][c] > maiorSegLinha:
                maiorSegLinha = matriz[l][c]
    print()
print('-='*15)
print(f'A soma dos valores pares é: {vPares}')
print(f'A soma dos valores da 3º coluna é: {terColuna}')
print(f'O maior valor da 2º linha é: {maiorSegLinha}')
