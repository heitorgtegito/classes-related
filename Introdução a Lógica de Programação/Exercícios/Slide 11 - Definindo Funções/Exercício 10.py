# 2, 4, 6, 8, 10
# 1, 3, 5, 7, 9
# 1, 3, 5, 7
# 2, 4, 6

def sequencia(a, b):
  if b % 2 == 0:
    for i in range(2, a * 2 + 1, 2):
      print(i, end=' ')
  else:
    for i in range(1, a * 2 + 1, 2):
      print(i, end=' ')
  print('')

sequencia(5, 2)
sequencia(5, 1)
sequencia(4, 3)
sequencia(3, 4)
