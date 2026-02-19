def listaa(A):
    listab = []
    for i in A:
        dobro = i * 2
        listab.append(dobro)
    return listab

print(listaa([2, 1, -1, 8]))
print(listaa([3, 1, -1, 5, 9, 13]))