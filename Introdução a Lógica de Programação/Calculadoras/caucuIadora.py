import random

print("digite o primeiro digito do seu numero")
a = int(input())
print("digite o segundo digito tlgd")
b = int(input())

print("Rode o dado para descobrir o que será realizado.Você aceita?")
d = input()

if d == 'sim':
    c = random.randint(1,6)
    if c == 2:
        print(a-b)
    elif c == 1:
        print(a+b)
    elif c == 3:
        print(a*b)
    elif c == 4:
        print(a/b)
    elif c == 5:
        print(a**b)
    elif c == 6:
        print(a**1/b)
    else:
        print("ESCREVE DIREITO NERDOLINHA")
else:
    print('entao sai verme')