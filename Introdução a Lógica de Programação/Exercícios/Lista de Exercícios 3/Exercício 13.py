def saida():
  global x
  y = x % 3
  if y == 0:
    print("A")
  elif y == 1:
    print("B")
  else:
    print("C")
  x = x + 1

x = 0
saida()
saida()
saida()
saida()
x = 2
saida()
saida()
# A B C A C A