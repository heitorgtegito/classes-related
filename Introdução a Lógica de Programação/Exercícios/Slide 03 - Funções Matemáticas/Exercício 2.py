import math

x = int(input('Por favor digite um número natural não nulo \t'))
if x < 1 :
    print('Tem que ser um número NATURAL e NÃO NULO!')
else:
    print(f' {x**2} é o quadrado do seu número; \n {math.sqrt(x)} é a raiz quadrada do seu número \n {x**(1/3)} é a raiz cúbica do seu número')