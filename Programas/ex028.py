print('-=-'*20)
print('Analisador de Triângulos')
print('-=-'*20)

cores = {'verde': '\033[32m',
         'vermelho': '\033[31m',
         'limpa': '\033[m'}

n1 = float(input('\nDigite o primeiro valor: '))
n2 = float(input('Digite o segundo valor: '))
n3 = float(input('Digite o terceiro valor: '))

if n3 < (n1+n2) and n1 < (n2+n3) and n2 < (n3+n1):
    print('{}Podem formar Triângulo{}'.format(cores['verde'], cores['limpa']))
else:
    print('{}Não podem formar Triângulo{}'.format(
        cores['vermelho'], cores['limpa']))
