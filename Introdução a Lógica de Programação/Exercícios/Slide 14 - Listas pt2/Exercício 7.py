def funcao(A,B):
    copia_a = A[:]
    sorted_b = B[:]
    sorted_b.sort(reverse=False)
    copia_a.clear()
    for m in sorted_b:
        for i in B:
            if m == i:
                indice_des = B.index(m)
                palavra = A[indice_des]
                copia_a.insert(0, palavra)
    return(copia_a)
    
print(funcao(['mamão', 'cajú', 'banana'],[5, 9, 1]))
print(funcao(['bola', 'casa', 'rato', 'boné'],[10, 20, 30, 40]))