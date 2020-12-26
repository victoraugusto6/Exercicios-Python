n = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razão da P.A.: '))
decimoTermo = n+(10-1)*r

for c in range(n, decimoTermo+r, r):
    print(c, end=' > ')
