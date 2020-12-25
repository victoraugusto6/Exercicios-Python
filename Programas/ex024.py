n = float(input('Digite a distância da sua viagem: '))

if (n <= 200):
    print(f'O valor da passagem é R${n*0.50}')
else:
    print(f'O valor da passagem é R${n*0.45}')
