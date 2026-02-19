def lista(A, B):
    interseccao = []
    for i in A:
        for c in B: 
            if c == i:
                if i not in interseccao:
                    interseccao.append(i)
    return interseccao

A = [2, 1, -1, 8]
B = [0, 2, 5, 6, 9, 1, 3]
print(lista(A,B))

A = [3, 1, -1, 5, 9, 13]
B = [0, 1, 5, 4, 5, 6, 5]
print(lista(A,B))

A = [2, 4, 6, 8, 10]
B = [1, 3, 5]
print(lista(A,B))

