def funcao(m,s):
    n_linhas = len(m)
    if n_linhas == 0:
        return None
    n_colunas = len(m[0])
    for l in range(n_linhas, 0, -1):
        for c in range(n_colunas, 0, -1):
            if m[l-1][c-1] == s:
                return l-1, c-1
    return None # m não contém s

a = [["bola", "casa", "lanche"], ["galho", "bola", "sol"]]
b = "bola"
c = [["bola", "casa", "lanche"], ["galho", "bola", "sol"]]
d = "lanche"
e = [["bola", "casa", "lanche"], ["galho", "bola", "sol"]]
f = "banana"

print(funcao(a,b))
print(funcao(c,d))
print(funcao(e,f))
