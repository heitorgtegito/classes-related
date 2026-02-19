def media(m):
    soma = 0
    termos = 0
    for i in range(len(m)):
        for j in range(len(m[i])):
            soma += m[i][j]
            termos += 1
    arit = soma/termos
    return arit
print(media([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]]))