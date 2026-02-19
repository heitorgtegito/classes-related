# Avaliação Prática - 3º Bimestre
# Heitor Egito - Informática para internet 2025.1 Vespertino
def funcao(L):
    impares = 0
    pares = 0
    for i in L:
        if i%2 == 0:
            pares += 1
        else:
            impares += 1
    return pares, impares


print('---------')
pares, impares = funcao([1,2,3,4,5])
print(pares)
print(impares)
print('---------')
pares, impares = funcao([2,4,6])
print(pares)
print(impares)
print('---------')
pares, impares = funcao([1,3,5])
print(pares)
print(impares)
print('---------')
pares, impares = funcao([])
print(pares)
print(impares)
print('---------')
pares, impares = funcao([1,2,3,4,5,6,7,8,9,10])
print(pares)
print(impares)
print('---------')

# # Extra!
# def impressao(L):
#     pares, impares = funcao(L)
#     print('---------')
#     print(pares)
#     print(impares)

# impressao([1,2,3,4,5])
# impressao([2,4,6])
# impressao([1,3,5])
# impressao([])
# impressao([1,2,3,4,5,6,7,8,9,10])