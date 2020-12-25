from math import sin, cos, tan, trunc, radians

ang = float(input('Digite um ângulo qualquer: '))
ang = radians(ang)

seno = (ang)
cosseno = cos(ang)
tangente = tan(ang)

print(f'Ângulo: {ang:.2f}\nSeno: {seno:.2f}\nCosseno: {cosseno:.2f}\nTangente: {tangente:.2f}')