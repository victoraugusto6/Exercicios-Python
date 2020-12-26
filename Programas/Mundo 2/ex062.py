primeiro = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razão da P.A.: '))
decimoTermo = primeiro+(10-1)*r
termo = primeiro
count = 1
total = 0
mais = 10

while mais != 0:
    total += mais
    while(count <= total):
        print(f'{termo} > ', end=' ')
        termo += r
        count += 1
    print('PAUSA')
    mais = int(input('Digite quantos termos a mais deseja ver: '))
print('FIM')
