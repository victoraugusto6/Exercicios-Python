def area(l, c):
    print(f'A área de um terreno {l}x{c} é de {l*c}m²')


print(' Controle de Terrenos')
print('-'*20)
largura = float(input('LARGURA (m): '))
comprimento = float(input('COMPRIMENTO (m): '))
area(largura, comprimento)
