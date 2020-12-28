exp = []
exp = input('Digite a expressão: ')
pa = exp.count('(')
pf = exp.count(')')

if(pa == pf):
    print(f'A expressão {exp} é válida')
else:
    print(f'A expressão {exp} não é válida')
