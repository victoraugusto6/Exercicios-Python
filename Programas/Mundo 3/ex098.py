from time import sleep


def contador(i, f, p):
    print('~'*30)
    if(p < 0):
        p *= -1
    if (p == 0):
        p = 1
    print(f'Contagem de {i} até {f} de {p} em {p}')
    sleep(2.5)
    if i < f:
        for v in range(i, f+1, p):
            print(v, end=' ', flush=True)
            sleep(0.5)
        print('FIM!')
    elif f < i:
        for v in reversed(range(f, i+1, p)):
            print(v, end=' ', flush=True)
            sleep(0.5)
        print('FIM!')


contador(1, 10, 1)
contador(10, 0, 2)
print('~'*30)
print('Agora é sua vez de personalizar a contagem!')
contador(int(input('Início: ')), int(input('Fim: ')), int(input('Passo: ')))
