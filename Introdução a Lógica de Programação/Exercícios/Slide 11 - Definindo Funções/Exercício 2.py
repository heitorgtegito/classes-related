a = int(input('Digite o primeiro número: '))
b = int(input('Digite o segundo número: '))

def mult(a,b):
    return a * b

m = mult(a,b)

print(f'{a} * {b} = {m}')

# teste 1
m = mult(12,2)
print('12 * 2 = ', m)

# teste 2 
m = mult(12,12)
print('12 * 12 =', m)