n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segundo nota: '))

media = (n1+n2)/2

print(f'Sua média foi: {media:.2f}')
if(media < 5):
    print('REPROVADO')
elif (media >= 5 and media <= 6.9):
    print('RECUPERAÇÂO')
else:
    print('APROVADO')
