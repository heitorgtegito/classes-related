def lidiv5(L):
    lista = []
    for i in L:
        if i%5 == 0:
            lista.append(i)
        else:
            lista = lista
    return lista

print(lidiv5([1, 1, 10, 15, 9]))
print(lidiv5([9, 1, -1, 8]))