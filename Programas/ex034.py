from datetime import date

ano = int(input('Digite seu ano de nascimento: '))
idade = date.today().year - ano

print('-=-'*10)
print('CATEGORIA')
print('-=-'*10)

print('\nVocê tem {} anos.'.format(idade))

if(idade <= 9):
    print('MIRIM')
elif (idade <= 14):
    print('INFANTIL')
elif(idade <= 19):
    print('JUNIOR')
elif (idade <= 20):
    print('SÊNIOR')
else:
    print('MASTER')
