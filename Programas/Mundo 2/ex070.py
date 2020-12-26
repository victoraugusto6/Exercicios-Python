# Vários produtos

escolha = produtoMaisBarato = nomeProduto = 'a'
c = totalGasto = maiorMil = precoMaisBarato = preco = 0


while True:
    nomeProduto = input('\nProduto: ')
    preco = float(input('Preço: R$'))

    totalGasto += preco

    if preco > 1000:
        maiorMil = +1

    if c == 0:
        produtoMaisBarato = nomeProduto
        precoMaisBarato = preco

    if(preco < precoMaisBarato):
        precoMaisBarato = preco
        produtoMaisBarato = nomeProduto

    while 's' not in escolha and 'n' not in escolha:
        escolha = input('Deseja continuar? [S/N]: ').lower().strip()
    if escolha == 'n':
        break
    escolha = 'a'
    c = 1
print(f'\nO total gasto na compra foi: R${totalGasto:.2f}')
print(f'A quantidade de produtos com valor maior de mil reais é: {maiorMil}')
print(
    f'O produto mais barato é o {produtoMaisBarato} com o valor de R${precoMaisBarato:.2f}')
