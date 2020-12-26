from datetime import date

ano = int(input('Digite seu ano de nascimento: '))
idade = date.today().year-ano

if(idade < 18):
    print(
        f'Você tem {idade} anos, então ainda irá se apresentar. Faltam {18-idade} anos para o grande dia.')
elif(idade == 18):
    print(f'Você tem {idade} anos, então está na hora de você se apresentar')
else:
    print(
        f'Você tem {idade} anos. Passou da hora de você se apresentar! Passaram {idade-18} anos para o alistamento.')
