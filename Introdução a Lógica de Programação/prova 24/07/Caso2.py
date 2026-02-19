a = int(input('Digite um número maior ou igual a 2 '))
n = int(input('Digite um número maior ou igual a 1 '))
o = 2
while n >= 1:
    resposta = f'{a} ** {o} = {a**o}'
    o = o + 1
    n = n - 1
    print(resposta)