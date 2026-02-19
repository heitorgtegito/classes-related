a = int(input('Digite um número inteiro: '))
x = 1
y = 0
while x <= a:
    if x%3 == 0:
        produto = y + x
        y = produto
        x = x + 1
    else:
        x = x + 1
print(produto)