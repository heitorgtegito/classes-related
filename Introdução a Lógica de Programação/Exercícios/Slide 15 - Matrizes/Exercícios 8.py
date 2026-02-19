def somar_primeira_coluna(m):
    n_colunas = len(m[0])
    n_linhas = len(m)
    c = n_colunas
    if n_colunas == 0:
        return None
    soma = 0
    for i in range(n_linhas):
        soma += m[i][c-1]
    return soma

a = [[1, 2, 3], [6, 7, 8]]
b = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
c = [[1, 0, 5, 4, 7]]
d = [[7], [10]]

print(somar_primeira_coluna(a))
print(somar_primeira_coluna(b))
print(somar_primeira_coluna(c))
print(somar_primeira_coluna(d))
