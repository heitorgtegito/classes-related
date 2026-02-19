a = int(input('Digite um valor: '))
b = int(input('Digite um valor: '))
c = int(input('Digite um valor: '))
d = int(input('Digite um valor: '))
e = int(input('Digite um valor: '))

def min_max(a,b,c,d,e):
    return min(a,b,c,d,e), max(a,b,c,d,e)

mn, mx = min_max(a,b,c,d,e)

print(mn)
print(mx)

# teste 1
a = 2
b = 5
c = 7
d = 12
e = 9
mn, mx = min_max(2,5,7,12,9)
print(mn) # Saída: 2
print(mx) # Saída: 12

# teste 2
a = 21
b = 243
c = -125
d = 12
e = 52234
mn, mx = min_max(21,243,-125,12,52234)
print(mn) # Saída: -125
print(mx) # Saída: 55234