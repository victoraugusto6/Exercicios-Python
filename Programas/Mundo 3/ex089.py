lista = list()
alunos = list()
alunoN = 0

while True:

    nome = input('Nome: ')
    lista.append(nome)
    n1 = float(input('Nota 1: '))
    lista.append(n1)
    n2 = float(input('Nota 2: '))
    lista.append(n2)
    alunos.append(lista[:])
    lista.clear()

    e = input('Deseja continuar? [S/N] ').lower()
    if e == 'n':
        break
print()
print('-='*5)
print('BOLETIM')
print('-='*5)
print(f'{"Nº":<4}{"Nome":<10}{"Média":>8}')
for i, aluno in enumerate(alunos):
    mediaAluno = (aluno[1]+aluno[2])/2
    print(f'{i:<4}{aluno[0]:<10}{mediaAluno:>8}')
while alunoN != 999:
    alunoN = int(input('Mostrar notas de qual aluno? (999 interrompe) '))
    for i, aluno in enumerate(alunos):
        if(i == alunoN):
            print(f'Notas de {aluno[0]}: [{aluno[1]}, {aluno[2]}]')
        else:
            print('Aluno não encontrado na lista!')
