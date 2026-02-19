def funcao(a):
  x = 0
  i = 1
  while i <= 4:
    if i == a:
      return x
    x = x + i
    i = i + 1
  return x

print(funcao(10))
print(funcao(3))
print(funcao(1))
# 10, 3, 0