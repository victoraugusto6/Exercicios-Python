# Vários produtos

escolha = produtoMaisBarato = 'a'
totalGasto = maiorMil = precoMaisBarato = 0


while True:
    nomeProduto = input('\nProduto: ')
    preco = float(input('Preço: R$'))

    produtoMaisBarato = nomeProduto
    precoMaisBarato = preco

    totalGasto += preco

    if preco > 1000:
        maiorMil = +1

    if(preco < precoMaisBarato):
        precoMaisBarato = preco
        produtoMaisBarato = nomeProduto

    while 's' not in escolha and 'n' not in escolha:
        escolha = input('Deseja continuar? [S/N]: ').lower().strip()
    if escolha == 'n':
        break
    escolha = 'a'
print(f'\nO total gasto na compra foi: R${totalGasto:.2f}')
print(f'A quantidade de produtos com valor maior de mil reais é: {maiorMil}')
print(
    f'O produto mais barato é o {produtoMaisBarato} com o valor de R${precoMaisBarato:.2f}')
