# a = int(input('Digite o Dividendo: '))
# b = int(input('Digite o Divissor: '))
# q = a / b
# print('Quociente', q)

# Modifique o programa pra não rolar o bug de dividir por 0 e dar erro

a = int(input('Digite o Dividendo: '))
b = int(input('Digite o Divisor: '))
if b == 0:
    print('Error')
else:
    q = a / b
    print('Quociente', q)