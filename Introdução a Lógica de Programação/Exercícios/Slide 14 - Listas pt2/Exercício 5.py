c = []
def funcao(a,b):
    for i in a:
        p = i 
        for i in b:
            if i != p:
                if c.count(p) < 1:
                    c.append(p)
                if c.count(i) > 0:
                    c.remove(i)
    return c

print(funcao([10, 20, 30, 40, 50], [15, 20, 25, 30]))