from datetime import date

pessoa = dict()

pessoa['nome'] = input('Nome: ')
pessoa['idade'] = date.today().year - int(input('Ano de Nascimento: '))
pessoa['ctps'] = int(input('Carteira de Trabalho (0 não tem): '))
if(pessoa['ctps'] > 0):
    pessoa['contratação'] = int(input('Ano de Contratação: '))
    pessoa['salário'] = float(input('Salário: R$'))
    pessoa['aposentadoria'] = pessoa['idade'] + \
        ((35+pessoa['contratação'])-date.today().year)
print('-='*20)
for k, v in pessoa.items():
    print(f' - {k} tem o valor {v}')
