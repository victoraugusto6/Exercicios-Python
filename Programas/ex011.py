from math import hypot

catOposto = float(input('Cateto Oposto: '))
catAdj = float(input('Cateto Adjascente: '))
h = hypot(catOposto,catAdj)

print(f'Hipotenusa: {h:.2f}')