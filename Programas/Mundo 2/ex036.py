print('-=-'*20)
print('Aprovar empréstimo de imóvel')
print('-=-'*20)

valorCasa = float(input('\nQual o valor da casa? R$'))
salario = float(input('Qual o salário do comprador? '))
anos = int(input('Em quantos antos deseja pagar? '))

# Prestação mensal
mesesPagando = (anos*12)
prestacao = valorCasa/mesesPagando
porcentual = (salario*(30/100))

print(
    f'Para pagar um imóvel de R${valorCasa:.2f} em {anos} anos será feito uma prestação de R${prestacao:.2f}\n')

if (prestacao <= porcentual):
    print(
        f'Ótimo! O empréstimo será efetuado no valor de R${prestacao:.2f}.')
else:
    print('Infelizmente, o empréstimo será negado.')
