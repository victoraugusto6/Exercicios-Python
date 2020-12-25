print('-='*15)
print('Sequência de Fibonacci')
print('-='*15)

n = int(input('Quantos termos quer mostrar?: '))
t1 = 0
t2 = 1
print('~'*30)
print(f'{t1} > {t2}', end='')
count = 3

while count <= n:
    t3 = t1+t2
    print(f' > {t3}', end='')
    t1 = t2
    t2 = t3
    count += 1

print(' > FIM')
