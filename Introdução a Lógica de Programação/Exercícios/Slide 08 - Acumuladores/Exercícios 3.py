x = 1
y = 0
while x <= 10:
    if x%2 == 0:
        soma = y + x
        y = soma
        x = x + 1
    else:
        x = x + 1
print(soma)