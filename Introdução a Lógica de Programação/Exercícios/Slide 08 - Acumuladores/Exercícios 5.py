x = 1
y = 1
while x <= 8:
    if x%2 == 0:
        x = x + 1
    else:
        produto = y * x
        y = produto
        x = x + 1
print(produto)