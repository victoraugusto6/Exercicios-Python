# Tabuada até digitar negativo
c = 0

while True:
    print(f'-'*15)
    n = int(input('Digite um número: '))
    print(f'-'*15)

    # Saída
    if(n < 0):
        break

    # Tabuada
    while(c <= 10):
        print(f'{n} x {c} = {n*c}')
        c += 1
    c = 0
