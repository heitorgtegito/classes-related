def funcao(m,a):
    soma = 0
    for i in range(len(m)):
        soma += m[i][a]
    return soma

n = [[1, 2, 3], [6, 7, 8]]
j = 0
o = [[1, 2, 3], [6, 7, 8]]
k = 1
p = [[10]]
l = 0
print(funcao(n,j))
print(funcao(o,k))
print(funcao(p,l))
