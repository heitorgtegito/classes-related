def media(L):
    soma = 0
    for i in L:
        soma += i
    dividido = soma/len(L)
    return dividido

# teste 1
print(media([4, 5, 3]))
# teste 2
print(media([1, 0, 9, 1, 5]))
