def notas(* notas, situacao):
    n = dict()
    n['total'] = len(notas)
    n['maior'] = max(notas)
    n['menor'] = min(notas)
    n['média'] = sum(notas)/len(notas)
    if situacao == True:
        if n['média'] >= 7:
            n['situação'] = 'BOM'
        elif n['média'] >= 5:
            n['situação'] = 'RAZOÁVEL'
        else:
            n['situação'] = 'RUIM'
    return n


resp = notas(9, 5, 5.5, 2.5, 10, situacao=True)
print(resp)
