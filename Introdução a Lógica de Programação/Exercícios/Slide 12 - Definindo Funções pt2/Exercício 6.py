def funcao(a, b, c=3, d=0):
  return a + b + c + d

l = funcao(1, 2)
print(l)

l = funcao(1, 2, 6)
print(l)

# l = funcao(10)
# print(l)

l = funcao(3, 2, d=10)
print(l)

l = funcao(3, 2, d=10, c=0)
print(l)

# l = funcao(d=10, c=0, 2, 1)
# print(l)

# l = funcao(a=10, 0, 2, 1)
# print(l)

l = funcao(a=10, d=3, c=1, b=5)
print(l)

l = funcao(5, b=3, d=1, c=2)
print(l)

#  6 9 Erro 18 15 Erro Erro 19 11
