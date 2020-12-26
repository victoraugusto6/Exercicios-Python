frase = '   Victor Augusto Soares de Oliveira   '

print(f'Frase original: {frase}')

# Escolher a primeira letra
print(frase[3])

# Imprime apenas 'Victor'
print(frase[:6])

# Imprime de 2 em 2
print(frase[::2])

# Frases longas
print('''Nessa aula, vamos aprender operações com String
no Python.''')

# Contando
print(frase.count('Victor'))

# Maíscula
print(frase.upper())

# Miníscula
print(frase.lower())

# Remover espaços nas extremidades
frase = frase.strip()
print(frase)

# Contar tamanho
print(len(frase))

# Substituir
print(frase.replace('Victor', 'Ana'))

# Dividir
print(frase.split())
