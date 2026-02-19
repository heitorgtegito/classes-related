a = int(input('Digite um número\n'))
b = int(input('Digite um outro número\n'))
c = int(input('Digite um último número\n'))
if a > b > c: # C em ultimo
    print(f'{c} {b} {a}')
elif a > b < c and a > c: # B em ultimo
    print(f'{b} {c} {a}')
elif a > b < c and c > a: # B em último
    print(f'{b} {a} {c}')
elif a < b < c: # A em ultimo
    print(f'{a} {b} {c}')
elif a < b > c and c > a: # A em último
    print(f'{a} {c} {b}')
elif a < b > c and a > c: # C em último
    print(f'{c} {a} {b}')
else:
    print('Error')