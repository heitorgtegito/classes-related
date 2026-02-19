import time

print("Seleciona o número dog")
time.sleep(2)
print(int(input())*2)
time.sleep(4)

print("Próximo:", "-" * 50)
time.sleep(2)
print(round(3*1.2,1))
time.sleep(4)

print("Próximo:", "-" * 50)
time.sleep(2)
print("Digite 3 números e eu somarei eles")
print(int(input()) + int(input()) + int(input()))
time.sleep(4)

print("Próximo:", "-" * 50)
time.sleep(2)
print("Digite 4 números e eu farei a média deles")
x = int(input()) + int(input()) + int(input()) + int(input())
print(round(x/4,1))
time.sleep(4)

print("Próximo:", "-" * 50)
time.sleep(2)
print("Qual seu nome?")
x = input()
a = len(x)
print("+" + "-" * a + "+" "\n" "|" + x + "|" "\n" "+" + "-" * a + "+" )
time.sleep(4)

print("Fim", "-" * 100)