# Fórmula: dividindo o peso (em kg) pela altura ao quadrado (em metros).

peso = float(input('Digite seu peso: '))
altura = float(input('Digite sua altura: '))
imc = peso/(pow(altura, 2))

print(
    f'Seu peso é {peso}kg e sua altura {altura}m, logo, seu IMC é: {imc:.2f}')

if (imc < 18.5):
    print('Abaixo do peso')
elif (18.5 <= imc and imc < 25):
    print('Peso ideal')
elif (25 <= imc and imc < 30):
    print('Sobrepeso')
elif (30 <= imc and imc < 40):
    print('Obesidade')
else:
    print('Obesidade mórbida, CUIDADO!')
