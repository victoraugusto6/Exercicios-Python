# Soma números até digitar 999
c = s = 0

while True:
    n = int(input('Digite um número. 999 irá cancelar a operação: '))
    if n == 999:
        break
    c += 1
    s += n
print(f'A quantidades de números digitados foi: {c}')
print(f'A soma dos números foi: {s}')
