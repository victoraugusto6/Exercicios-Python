n = 0
c = 0
s = 0

while(n != 999):
    n = int(input('Digite um número: '))
    if(n != 999):
        c += 1
        s += n
print(f'\nForam digitados {c} números')
print(f'A soma desses números é: {s}')
