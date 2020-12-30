def fatorial(n, show):
    print('-'*30)
    f = 1
    for c in range(n, 0, -1):
        f *= c
        if show == True:
            print(c, end='')
            if c > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
    return f
    if show == False:
        return f


print(fatorial(8, True))
