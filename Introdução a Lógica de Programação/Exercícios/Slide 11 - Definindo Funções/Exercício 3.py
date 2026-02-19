a = int(input('Digite um valor inteiro: '))

def div(a):
    return a%2

if div(a) == 0:
    print('Par')
else:
    print('Ímpar')

# teste 1:
div(2) # 2%2 == 0
print('Par')

#  teste 2:
div(4) # 4%2 == 0
print('Par')