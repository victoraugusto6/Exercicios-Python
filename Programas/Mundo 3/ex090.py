aluno = dict()

aluno['Nome'] = input('Nome: ')
aluno['Média'] = float(input('Média: '))
print('-='*20)
if(aluno['Média'] >= 7):
    aluno['Situação'] = 'Aprovado'
elif(aluno['Média'] >= 5 and aluno['Média'] < 7):
    aluno['Situação'] = 'Recuperação'
elif(aluno['Média'] < 5):
    aluno['Situação'] = 'Reprovado'
for k, v in aluno.items():
    print(f' - {k} é igual a {v}')
