valor = float(input('Valor a ser pago: R$'))
metPagamento = int(input('''Selecione a forma de pagamento:
1 - À vista (dinheiro ou Cheque)
2 - À vista (cartão)
3 - Em até 2x no cartão
4 - Em 3x ou mais no cartão\n'''))

if metPagamento == 1:
    novoValor = valor-(valor*(10/100))
    print(f'De R${valor:.2f} você pagará R${novoValor:.2f}.')
elif metPagamento == 2:
    novoValor = valor-(valor*(5/100))
    print(f'De R${valor:.2f} você pagará R${novoValor:.2f}.')
elif metPagamento == 3:
    print(f'Você pagará R${valor:.2f}.')
else:
    novoValor = valor+(valor*(20/100))
    print(f'De R${valor:.2f} você pagará R${novoValor:.2f}.')
