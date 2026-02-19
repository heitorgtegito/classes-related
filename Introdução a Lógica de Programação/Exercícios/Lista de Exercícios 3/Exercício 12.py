def funcao(a1, n):
  an = a1 + (n - 1) * r # 11
  s = n * (a1 + an) / 2 # 35
  return s

r = 2
i = 3
q = 5
s = 0
funcao(i, q) # Isso dá 35, mas nao tá definindo nada tlgd, por isso q dá 0
print(s) # 0
s = funcao(i, q) #35
print(s) # 35
# 0 35