v1 = [-1, -1, -1, -1, -1]
for c in range(0, 5):
    n = int(input('Digite um número: '))
    v1.insert(n, n)
for c in v1:
    v1.remove(-1)
print(v1)
