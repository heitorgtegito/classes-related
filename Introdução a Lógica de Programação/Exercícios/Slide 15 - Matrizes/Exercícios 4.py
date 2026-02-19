def somar_primeira_linha(m):
    if len(m) == 0 or len(m[0]) == 0:
        return None
    elif len(m) == 1 or len(m[1]) == 1:
        return None
    soma = sum(m[1])
    return soma

a = [[1, 2, 3], [6, 7, 8]]
b = [[1, 1], [2, 3], [0, 10]]
c = [[1, 0, 5]]
print(somar_primeira_linha(a))    
print(somar_primeira_linha(b))   
print(somar_primeira_linha(c))
