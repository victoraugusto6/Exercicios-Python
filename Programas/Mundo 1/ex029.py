velocidade = float(input('Digite a velocidade de um carro: '))

if velocidade > 80:
    print(
        f'\033[31mVocê foi multado por passar em {velocidade:.2f}Km/h numa estrada de 80Km/h!\nPague o valor de R${(velocidade-80)*7:.2f}\033[m')

print('\033[1;32mTenha um bom dia!\033[m')
