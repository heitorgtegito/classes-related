n = int(input('Digite um número inteiro positivo: '))
x = 1
while x <= n:
    if x%3 == 0 and x%4 == 0:
        print("FizzBuzz")
        x = x + 1
    elif x%4 == 0:
        print("Buzz")
        x = x + 1
    elif x%3 == 0:
        print("Fizz")
        x = x + 1
    else:
        print(x)
        x = x + 1