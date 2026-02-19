def som(L):
    soma = 0
    for i in L:
        if i%3 == 0:
            soma = soma + i
        else:
            soma = soma
    return soma

print(som([0, 6, -1, 12, 1]))
print(som([0, 1, -1, 8]))