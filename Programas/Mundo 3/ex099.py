from time import sleep


def linha():
    print('-=-'*30)


def maior(*num):
    linha()
    maior = 0
    print(f'Analisando os valores passados...')
    for v in num:
        print(v, end=' ', flush=True)
        sleep(0.5)
        if v > maior:
            maior = v
    print(f' Foram informados {len(num)} valores ao todo.')
    print(f'O maior número foi: {maior}')


maior(0, 5, 8, 9, 300, 22, 5, 44, 99)
maior(0)
maior(2, 5)
