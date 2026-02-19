a = int(input('Digite um número\n'))
b = int(input('Digite um outro número\n'))
c = a + b
d = c%2
if d == 0:
    print(f'A soma é par')
else:
    print(f'A soma é ímpar')