# A
x = float(input())
dobro = x * 2
triplo = x * 3
print(dobro)
print(triplo)

# B
soma_angulos = float(input())
if soma_angulos == 180:
    print('É triângulo')
else:
    print('Não é triângulo')

# C
media = float(input())
if media >= 60:
    print('Aprovado')
elif media >= 30:
    print('Em recuperação')
else:
    print('Reprovado')

# D
n = float(input())
soma = 0
while n > 0:
    soma = soma + n
    n = float(input())
print(soma)