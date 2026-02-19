def somar_matriz(m):
  soma = 0
  for i in range(len(m)):
    for j in range(len(m[i])):
        if m[i][j]%2 == 0:
            soma += m[i][j]
  return soma

print(somar_matriz([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]]))