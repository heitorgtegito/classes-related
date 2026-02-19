a = int(input('Digite um número inteiro: '))
x = 1
y = 2**0
soma = x
if a >= 0:
    while x <= a:
        soma = y + 2**x
        y = soma
        x = x + 1
    print(soma)
else:
    print('Error')