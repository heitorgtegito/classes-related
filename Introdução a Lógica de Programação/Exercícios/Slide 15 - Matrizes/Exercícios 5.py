def somar_primeira_linha(m):
    n = len(m) - 1
    if len(m) == 0:
        return None
    soma = sum(m[n])
    return soma

a = [[1, 2, 3], [6, 7, 8]]
b = [[1, 1], [2, 2], [3, 3]]
c = [[1, 0, 5, 3]]
print(somar_primeira_linha(a))    
print(somar_primeira_linha(b))   
print(somar_primeira_linha(c))
