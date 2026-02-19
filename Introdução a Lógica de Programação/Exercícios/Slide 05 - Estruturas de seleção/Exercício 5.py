a = int(input('Digite um número\n'))
b = int(input('Digite um outro número\n'))
if a > b:
    print(f'{b} {a}')
elif a == b:
    print(f'Os dois números são iguais')
else:
    print(f'{a} {b}')