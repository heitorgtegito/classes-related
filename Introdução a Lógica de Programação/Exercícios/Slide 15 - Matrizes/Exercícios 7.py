def somar_primeira_coluna(m):
    n_colunas = len(m[0])
    n_linhas = len(m)
    if n_colunas == 0 or n_colunas == 1:
        return None
    soma = 0
    for i in range(n_linhas):
        soma += m[i][1]
    return soma

a = [[1, 2, 3], [6, 7, 8]]
c = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
d = [[1, 0, 5, 9, 6]]
e = [[7], [15], [9]]

print(somar_primeira_coluna(a))
print(somar_primeira_coluna(c))
print(somar_primeira_coluna(d))
print(somar_primeira_coluna(e))
