n = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razão da P.A.: '))
decimoTermo = n+(10-1)*r
c = 0

while(n != decimoTermo+r):
    c += 1
    print(f'Termo {c}: {n}')
    n += r
