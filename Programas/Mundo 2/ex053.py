f = input('Digite um frase: ').lower()
f = f.replace(' ', '')
tam = len(f)
p = ''

for c in range(tam-1, -1, -1):
    p += f[c]

print(f'{f} ao contrário é: {p}')
if(f == p):
    print('Logo, é Palíndromo!')
else:
    print('Logo, não é Palíndromo')
