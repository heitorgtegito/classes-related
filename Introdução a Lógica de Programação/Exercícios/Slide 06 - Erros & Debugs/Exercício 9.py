# # Programa que calcula as raízes de uma equação do 2º grau
# import math
# a = float(input('Coeficiente de x ao quadrado: '))
# b = float(input('Coeficiente de x: '))
# c = float(input('Coeficiente livre: '))
# delta = b ** 2 - 4 * a * b
# if delta < 0:
#   print('A equação não possui raízes reais.')
# elif delta == 0:
#   x = -b / 2 * a
#   print(f'Raíz: {x:.4f}')
# else:
#   x1 = -b + math.sqrt(delta) / 2 * a
#   x2 = -b - math.sqrt(delta) / 2 * a
#   print(f'Raiz 1: {x1:.4f}')
#   print(f'Raiz 2: {x1:.4f}')

# Programa que calcula as raízes de uma equação do 2º grau
import math
a = float(input('Coeficiente de x ao quadrado: '))
b = float(input('Coeficiente de x: '))
c = float(input('Coeficiente livre: '))
delta = b ** 2 - 4 * a * c
if delta < 0:
  print('A equação não possui raízes reais.')
elif delta == 0:
  x = -b / 2 * a
  print(f'Raíz: {x:.4f}')
else:
  x1 = (-b + (delta**0.5)) / 2 * a
  x2 = (-b - (delta**0.5)) / 2 * a
  print(f'Raiz 1: {x1:.4f}')
  print(f'Raiz 2: {x2:.4f}')
