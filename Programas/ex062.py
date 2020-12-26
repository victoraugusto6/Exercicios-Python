# Programa que leia Idade e Sexo de pessoas
c = maiorIdade = qtdHomens = qtdMulheres = 0
sexo = 'a'

while True:
    idade = int(input(f'Digite a idade da pessoa {c+1}: '))

    if(idade >= 18):
        maiorIdade += 1

    while 'm' not in sexo and 'f' not in sexo:
        sexo = input(f'Digite o sexo da pessoa {c+1} [M/F]: ').lower().strip()
        c += 1
        if 'm' in sexo:
            qtdHomens = +1
        elif 'f' in sexo and idade < 20:
            qtdMulheres += 1
    escolha = input('Deseja continuar? [S/N] ').lower().strip()
    if escolha == 'n':
        break
    sexo = 'a'

print(f'O número de pessoas maiores de idade são: {maiorIdade}')
print(f'Foram cadastrados {qtdHomens} homens')
print(f'Foram cadastrados {qtdMulheres} mulheres com menos de 20 anos')
