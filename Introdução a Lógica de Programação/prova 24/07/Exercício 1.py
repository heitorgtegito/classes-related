a = int(input())
b = int(input())

resposta = f''
while a > 1:
    resultado = a**b
    resposta = f'{a} ** {b} = {resultado} '
    a = a - 1
    print(resposta)