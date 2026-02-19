def funcao(L):
    C = L[:]
    L.reverse()
    if C == L:
        return True
    else:
        return False


print(funcao([1, 2, 2, 1]))
print(funcao([]))
print(funcao([3]))
print(funcao([1, 2, 3]))
print(funcao([1, -1]))