# 1
from tkinter import N


a = int(input('Digite um valor inteiro positivo '))
x = a - 1
resposta = ' '
if a > 0:
    resposta = f'{a} '
    while x > 0:
        resposta = resposta + f'{x} '
        x = x - 1
    print(resposta)
else:
    print('Error')


# 2
a = int(input('Digite um valor inteiro positivo '))
x = a - 1
resposta = ' '
if a < 0:
    print('Error')
else:
    resposta = f'{a} '
    while x > 0:
        if a%x == 0:
            resposta = resposta + f'{x} '
            x = x - 1
        else:
            x = x - 1
print(resposta)

# 3
a = int(input('Digite um valor inteiro positivo '))
x = 0
if a > 0:
    while x < a:
        print(f'{4*x}')
        x = x + 1
else:
    print('Error')

# 4 
a = int(input('Digite o primeiro valor inteiro positivo: '))
b = int(input('Digite o segundo valor inteiro positivo: '))
x = 0
if a > 0 and b > 0:
    while x < b:
        print(f'{a*x}')
        x = x + 1
else:
    print('Error')

# 5
a = int(input('Digite o primeiro valor inteiro positivo: '))
b = int(input('Digite o segundo valor inteiro positivo: '))
if a > 0 and b > 0:
    if a > b:
        x = b
        while x > 0:
            if a%x == 0 and b%x == 0:
                print(f'{x} é o MDC')
                x = x - x
            else:
                x = x - 1
    else:
        x = a
        while x > 0:
            if a%x == 0 and b%x == 0:
                print(f'{x} é o MDC')
                x = x - x
            else:
                x = x - 1
else:
    print('Error')

# 2º Método

# a = int(input('Digite o primeiro valor inteiro positivo: '))
# b = int(input('Digite o segundo valor inteiro positivo: '))
# x = 2
# y = 1
# resposta = f' '
# if a > 0 and b > 0: # Esse primeiro IF é pra brekar o codigo se o input for 0 ou negativo.
#     while x < 100000:
#         if a%x == 0 and b%x == 0:
#             fatores = y * x
#             y = y * x
#             a = a/x
#             b = b/x
#             while a%x == 0 and b%x == 0:
#                 fatores = y * x
#                 y = y * x
#                 a = a/x
#                 b = b/x
#             x = x + 1
#         else:
#             x = x + 1
#     print(fatores)
# else:
#     print('Error')

# 6
a = int(input('Digite o primeiro valor inteiro positivo: '))
b = int(input('Digite o segundo valor inteiro positivo: '))
x = 1
if a > 0 and b > 0:
    if a == b:
        print(f'{a} é o MMC')
    else:
        menorA = a * x
        menorB = b * x
        if menorA < menorB:
            while menorA != menorB:
                menorA = a * x
                x = x + 1
            print(f'{menorA} é o MMC')
        else:
            while menorA != menorB:
                menorB = b * x
                x = x + 1
            print(f'{menorA} é o MMC')
else:
    print('Error')

# 7
a = int(input('Digite um número inteiro positivo: '))
if a <= 0:
    print('Error')
else:
    x = 1
    y = 1
    seq = f'{x}'
    a = a - 1 
    while a > 0:
        x = y - x
        y = x + y
        seq = f'{seq} {y}'
        a = a - 1
    print(seq)

# 8
a = int(input('Digite um número inteiro positivo: '))
if a <= 0:
    print('Error')
else:
    n = 0
    while n <= 10:
        print(f'{a} x {n} = {a * n}')
        n = n + 1

# 9 
a = int(input('Digite um número real: '))
if a < 0:
    print('Informe um valor não-negativo')
    a = a * -1
    print(round(a**(1/2),2))
else:
    print(round(a**(1/2),2))

# 10
a = int(input('Digite um número inteiro positivo: '))
if a <= 0:
    print('Error')
else:
    n = 1
    while a > 0:
        print('*' * n)
        a = a - 1
        n = n + 1

# 11
a = int(input('Digite um número inteiro positivo: '))
if a <= 0:
    print('Error')
else:
    n = 1
    while a > 0:
        print(' ' * (a-1) + '*' * n)
        a = a - 1
        n = n + 1

# 12
a = int(input('Digite um número inteiro positivo: '))
if a <= 0:
    print('Error')
else:
    n = 1
    while a > 0:
        print(' ' * (a-1) + '*' * (n*2 - 1) + ' ' * (a-1))
        a = a - 1
        n = n + 1
        
# 13
a = int(input('Digite um número inteiro positivo: '))
if a <= 0:
    print('Error')
else:
    n = 2
    seq = 1
    resposta = f'{seq}'
    while a > 0:
        resposta = f'{seq} {n}'
        print(seq)
        seq = resposta
        n = n + 1
        a = a - 1


# 14
a = int(input('Digite um número inteiro positivo: '))
if a <= 0:
    print('Error')
else:
    n = a
    seq = f'{a}'
    resposta = f''
    while a > 0:
        if n > 0:
            seq = f'{n} '
            resposta = resposta + seq
            if n == 1:
                print(resposta)
                resposta = f''
                n = n - 1
            else:
                n = n - 1
        else:
            a = a - 1
            n = a

# 15
a = int(input('Digite um valor inteiro pertencente ao intervalo [0,2]'))
b = int(input('Digite um segundo valor inteiro pertencente ao intervalo [0,2]'))
if 3 > a > -1 and 3 > b > -1:
    resposta1 = f''
    resposta2 = f''
    resposta3 = f''
    resposta4 = f''
    resposta5 = f''
    resposta6 = f''
    resposta7 = f''
    if a == 0:
        resposta1 = f' *** 	'
        resposta2 = f'*   *	'
        resposta3 = f'*   *	'
        resposta4 = f'*   *	'
        resposta5 = f'*   *	'
        resposta6 = f'*   *	'
        resposta7 = f' *** 	'
    elif a == 1:
        resposta1 = f'  *   '
        resposta2 = f' **   '
        resposta3 = f'  *   '
        resposta4 = f'  *   '
        resposta5 = f'  *   '
        resposta6 = f'  *   '
        resposta7 = f' ***  '
    else:
        resposta1 = f' ***  '
        resposta2 = f'*   * '
        resposta3 = f'    * '
        resposta4 = f'   *  '
        resposta5 = f'  *   '
        resposta6 = f' *    '
        resposta7 = f'***** '
    if b == 0:
        resposta1 = resposta1 + f' *** 		'
        resposta2 = resposta2 + f'*   *		'
        resposta3 = resposta3 + f'*   *		'
        resposta4 = resposta4 + f'*   *		'
        resposta5 = resposta5 + f'*   *		'
        resposta6 = resposta6 + f'*   *		'
        resposta7 = resposta7 + f' *** 		'
    elif b == 1:
        resposta1 = resposta1 + f'  *  '
        resposta2 = resposta2 + f' **  '
        resposta3 = resposta3 + f'  *  '
        resposta4 = resposta4 + f'  *  '
        resposta5 = resposta5 + f'  *  '
        resposta6 = resposta6 + f'  *  '
        resposta7 = resposta7 + f' *** '
    else:
        resposta1 = resposta1 + f' *** '
        resposta2 = resposta2 + f'*   *'
        resposta3 = resposta3 + f'    *'
        resposta4 = resposta4 + f'   * '
        resposta5 = resposta5 + f'  *  '
        resposta6 = resposta6 + f' *   '
        resposta7 = resposta7 + f'*****'
    print(resposta1)
    print(resposta2)
    print(resposta3)
    print(resposta4)
    print(resposta5)
    print(resposta6)
    print(resposta7)
else:
    print('Digite numeros válidos na próxima')

# 16
a = int(input('Digite um valor inteiro positivo '))
even = 0
odd = 0
if a > 0:
    while a > 0:
        if a%2 == 0:
            even = even + a
            a = a - 1
        else:
            odd = odd + a
            a = a - 1
    print(f'A soma dos pares: {even}')
    print(f'A soma dos impares: {odd}')
else:
    print('Error')

# 17
a = int(input('Digite um valor inteiro '))
b = int(input('Digite um segundo valor inteiro '))
soma = 0
if a > b:
    n = a
    while n >= b:
        soma = soma + n 
        n = n - 1
    print(soma)
elif b > a:
    n = b
    while n >= a:
        soma = soma + n
        n = n - 1
    print(soma)
else:
    print('Não há intervalo')

# 18
a = int(input('Digite um valor inteiro para somar '))
soma = 0
while a != 0:
    soma = soma + a
    a = int(input('Digite mais um valor inteiro para somar ou digite 0 para parar '))
print(soma)

# 19
a = int(input('Digite um número inteiro positivo maior do que 1 '))
n = 1
if a <= 1:
    print('Informe um valor maior do que 1')
else:
    resposta = f''
    soma = 0
    while n < a:
        resposta = resposta + f'{n} + '
        soma = soma + n
        n = n + 1
    resposta = resposta + f'{n}'
    soma = soma + n
    print(f'{resposta} = {soma}')

# 20
a = int(input('Digite um número inteiro positivo maior do que 3 '))
n = 1
if a <= 3:
    print('Informe um valor maior do que 3')
else:
    rI = f''
    sI = 0
    rP = f''
    sI = 0
    while n <= a:
        if n%2 == 0:
            rP = rP + f'{n} + '
            sP = sP + n
            n = n + 1
        else:
            rI = rI + f'{n} + '
            sI = sI + n
            n = n + 1
    print(f'{resposta} = {soma}')

# 21
a = int(input('Digite um número inteiro positivo maior do que 1 '))
n = 1
if a <= 1:
    print('Informe um valor maior do que 1')
else:
    soma = n
    resposta = f'{n}'
    while n < a:
        n = n + 1
        resposta = resposta + f' + {n}'
        soma = soma + n
        print(f'{resposta} = {soma}')

# 22 -> 2 5 8 11
# 23 -> 22
# 24 -> -2 -1 1 2 Fim
# 25 -> 0 1 2 3
# 26 -> -2 -1 1 2
# 27 -> ### ## # Fim
# 28 -> 12
# 29 -> 18 12
# 30 -> 24
# 31 -> F(2) = 2 F(3) = 6 F(4) = 24 Fim