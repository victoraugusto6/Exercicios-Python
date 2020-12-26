n = int(input('Digite um número: '))
f = 1
while(n != 0):
    print(n, end=' ')
    f *= n
    n -= 1
print(f'\n{f}')
