e = 's'
lista = list()
dado = list()
nomeMaior = list()
nomeMenor = list()
maiorP = menorP = 0

while e == 's':
    dado.append(input('Digite um nome: '))
    dado.append(float(input('Digite um peso: ')))
    lista.append(dado[:])
    dado.clear()
    e = input('Deseja continuar? [S/N] ')
    if(e == 'n'):
        break

menorP = lista[0][1]
for p in lista:
    if(p[1] > maiorP):
        maiorP = p[1]
    if(p[1] < menorP):
        menorP = p[1]

for p in lista:
    if p[1] == maiorP:
        nomeMaior.append(p[0])
    elif p[1] == menorP:
        nomeMenor.append(p[0])

print(f'\nAo todo, você cadastrou {len(lista)} pessoas')
print(f'O maior peso foi de {maiorP} kg. Peso de {nomeMaior}')
print(f'O menor peso foi de {menorP} kg. Peso de {nomeMenor}')
