e = 'S'
s = quant = quant = maior = menor = media = 0

while(e == 'S'):

    n = int(input('Digite um número: '))
    s += n
    quant += 1

    if(quant == 1):
        maior = menor = n
    else:
        if(n > maior):
            maior = n
        if(n < menor):
            menor = n
    e = input('Deseja continuar? [S/N]: ').upper().strip()[0]

print(f'Voquantê digitou {quant} números')
print(f'A média destes números é: {s/quant}')
print(f'O menor valor foi: {menor}')
print(f'O maior valor foi: {maior}')
