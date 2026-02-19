def funcao(M):
    lista = []
    for i in range(len(M)):
        a = M[i]
        a.sort(reverse=True)
        lista.append(a[0])
    lista.sort(reverse=True)
    maior = lista[0]
    for i in range(len(M)):
        for j in range(len(M[i])):
            if M[i][j] == maior:
                return i, j
um = [[1, 2, 3], [4, 5, 6], [100, 0, 0]]
dois = [[100, 0, 0, 20], [0, 100, 0, 50]]
print(funcao(um))
print(funcao(dois))
