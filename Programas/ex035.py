from time import sleep

n1 = float(input('Primeira medida: '))
n2 = float(input('Segunda medida: '))
n3 = float(input('Terceira medida: '))

# Conferindo se podem formar triângulo

if(n1 < (n2+n3) and n2 < (n1+n3) and n3 < (n1+n2)):
    print('Ótimo! As medidas podem formar um triângulo.')

    print('E o tipo de triângulo é...')

    sleep(3)

    if(n1 == n2 and n3 == n1):
        print('Lados iguais. Logo podem formar um triângulo EQUILÁTERO')
    elif (n1 == n2 or n1 == n3 or n2 == n1 or n2 == n3):
        print('Dois lados iguais. Logo podem formar um triângulo ISÓSCELES')
    else:
        print('Lados diferentes. Logo podem formar um triângulo ESCALENO')
else:
    print('As medidas não podem formar um triângulo.')
