def funcao(l):
    for i in l[:]:
        if i%2 != 0:
            a = l.index(i)
            l.pop(a)
    return l

print(funcao([1,2,3,4,5,6]))
print(funcao([3,5,9,11]))
print(funcao([10,20,30,40,50]))