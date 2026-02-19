# Programa que informa se a entrada é um múltiplo de 3 e/ou de 5
n = int(input('Entrada: '))
if n % 3 == 0 and n % 5 == 0:
  print(f'{n} é múltiplo de 3 e de 5')
elif n % 5 == 0:
  print(f'{n} é múltiplo de 5')
elif n % 3 == 0:
  print(f'{n} é múltiplo de 3')
else:
  print(f'{n} não é múltiplo nem de 3 nem de 5')

#  O erro tá na ordem, o que ambos são múltiplos tem q vir primeiro