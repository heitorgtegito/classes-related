n = int(input('Digite um número inteiro positivo: '))
x = 1
while x <= n:
    if x%3 == 0:
        print(x)
        x = x + 1
    else:
        x = x + 1