a = int(input('Digite um número inteiro: '))
x = 1
y = 1
while x <= a:
    produto = y * x
    y = produto
    x = x + 1
print(produto)