# Entrada dos cinco números inteiros
a = int(input('Digite o primeiro número: '))
b = int(input('Digite o segundo número: '))
c = int(input('Digite o terceiro número: '))
d = int(input('Digite o quarto número: '))
e = int(input('Digite o quinto número: '))

# Organizando os números em ordem crescente sem usar sorted()
menor = min(a, b, c, d, e)
maior = max(a, b, c, d, e)

# Somando os três números centrais
soma = a + b + c + d + e - menor - maior

# Calculando a média
media = soma / 3

# Exibindo o resultado
print(f'A média dos três números centrais é: {media}')