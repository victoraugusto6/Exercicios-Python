def voto(ano):
    from datetime import date

    print('-'*20)
    idade = date.today().year - ano
    print(f'Idade = {idade} anos')
    if idade >= 18 and idade < 65:
        return 'Voto obrigatório'
    if idade < 16:
        return 'Voto Negado'
    else:
        return 'Voto Opcional'


ano = int(input('Digite seu ano de nascimento: '))
print(voto(ano))
