"""1. Ler quatro números inteiros, calcular a soma dos números pares e a soma dos números ímpares.
Digite quatro valores inteiros
1
2
3
4
Soma dos pares = 6
Soma dos ímpares = 4

2. Ler o número do mês (1 – janeiro; 2 – fevereiro; ...; 12 – dezembro) e identificar o nome do mês e em que trimestre
o mês está incluído.
Informe o número do mês
1
O mês de janeiro é do primeiro trimestre do ano

3. Ler 4 valores inteiros diferentes e realizar as seguintes operações: verificar se os valores são realmente diferentes
e mostrar uma mensagem de erro, caso contrário; mostrar o maior valor lido; mostrar o menor valor lido e mostrar o
resultado da soma entre o segundo maior valor e o segundo menor.
Digite quatro valores inteiros
1
2
3
10
Maior valor = 10
Menor valor = 1
A soma do segundo maior valor com o segundo menor = 5

4. Ler uma data no formato "dd/mm/aaaa" e verificar se é uma data válida, considerando como válidos os anos entre
1900 e 2100, meses de 1 a 12 e dias de acordo com o mês.
Digite uma data no formato dd/mm/aaaa
32/08/2013
A data informada não é válida

5. Ler três valores e mostrar em ordem crescente (sem usar o sort da linguagem)
Digite três valores:
10
2
15
2, 10, 15

6. Mostrar a sequência de números abaixo.
Resultado: 1 -2 3 -4 5 -6 7 -8 9 -10

7. Ler uma frase e mostrar as strings obtidas a partir desta, removendo uma a uma a palavra no início.
Digite uma frase:
Técnico em Informática para Internet
Técnico em Informática para Internet
em Informática para Internet
Informática para Internet
para Internet
Internet

8. Ler uma frase e mostrar as strings obtidas a partir desta, passando uma a uma a letra inicial para o final, até que
a frase inicial seja apresentada.
Digite uma frase:
Brasil
rasilB
asilBr
silBra
ilBras
lBrasi
Brasil

9. Ler uma frase e mostrar cada uma de suas palavras separadamente e de trás para frente.
Digite uma frase:
Técnico em Informática para Internet
ocincéT
me
acitámrofni
arap
tenretnI

10. Mostrar a sequência de números abaixo.
Resultado: 1
2 2
3 2
4 2 4
5 2 4
6 2 4 6
...
10 2 4 6 8 10
Obs: Primeira coluna: números de 1 a 10, demais colunas: números pares menores/iguais ao valor da 1a coluna.

11. Calcular a diagonal de um retângulo, dados a sua base b e sua altura h, utilizando a função Diagonal abaixo:
def Diagonal(b, h)

12. Obter o menor inteiro que seja maior ou igual ao número real x, utilizando a função MenorInteiro abaixo:
def MenorInteiro(x)

13. Remover espaços desnecessários entre palavras de um texto.
def RemoverEspacos(texto)

14. Obter o menor múltiplo comum (MMC) entre dois inteiros positivos x e y, utilizando a função MMC abaixo:
def MMC(x, y)

15. Verificar se um número é primo, utilizando a função Primo, abaixo:
def Primo(n)"""

# 1
print("Digite quatro valores inteiros")
n1 = int(input())
n2 = int(input())
n3 = int(input())
n4 = int(input())
respostas = [n1, n2, n3, n4]
soma_pares = 0
soma_impares = 0
for i in respostas:
    if i%2 == 0:
        soma_pares += respostas[i-1]
    else:
        soma_impares += respostas[i-1]
print(f"Soma dos pares = {soma_pares}")
print(f"Soma dos ímpares = {soma_impares}\n")

# 2
mes = int(input("Informe o número do mês\n"))
while mes < 1 or mes > 12:
    print("ERRO! Digite um número válido.")
    mes = int(input())
meses = ["janeiro", "fevereiro", "março", "abril", "maio", "junho", "julho", "agosto", "setembro", "outubro", "novembro", "dezembro"]
qualmes = meses[mes-1]
if mes <= 3:
    trimestre = "primeiro"
elif 3 < mes <= 6:
    trimestre = "segundo"
elif 6 < mes <= 9:
    trimestre = "terceiro"
elif 9 < mes <= 12:
    trimestre = "quarto"
print(f"O mês de {qualmes} é do {trimestre} trimestre do ano\n")

# 3
print("Digite quatro valores inteiros")
lista = []
for i in range(4):
    x = int(input())
    if x in lista:
        print("ERRO! Valores iguais foram digitados")
    else:
        lista.append(x)
lista.sort()
print(f"Maior valor = {lista[3]}")
print(f"Menor valor = {lista[0]}")
print(f"A soma do segundo maior valor com o segundo menor = {lista[1] + lista[2]}")

# 4
data = input("Digite uma data no formato dd/mm/aaaa\n")
data = data.split("/")
data[0] = int(data[0])
data[1] = int(data[1])
data[2] = int(data[2])
if data[0] > 31 or data[0] < 1 or data[1] > 12 or data[1] < 1 or data[2] > 2100 or data[2] < 1900:
    print("A data informada não é válida")
else:
    print("A data informada é válida")

# 5
print(f"Digite três valores:")
lista = []
for i in range(3):
    entrada = int(input())
    lista.append(entrada)
menor = lista[0]
if lista[1] < lista[0] and lista[1] < lista[2] : menor = lista[1]
if lista[2] < lista[0] and lista[2] < lista[1]  : menor = lista[2]
maior = lista[2]
if lista[0] > lista[2] and lista[0] > lista[1]  : maior = lista[0]
if lista[1] > lista[2] and lista[1] > lista[0]  : maior = lista[1]
lista.remove(menor)
lista.remove(maior)
meio = lista[0]
print(f'{menor}, {meio}, {maior}')

# 6
lista = []
for i in range(1, 11):
    if i%2 == 0 : i = -i
    lista.append(i)
print(*lista)

# 7
entrada = input("Digite uma frase\n")
entrada = entrada.split(' ')
for i in range(len(entrada)):
    print(*entrada)
    entrada.pop(0)

# 8
entrada = input("Digite uma frase\n")
for i in range(len(entrada)):
    entrada = entrada[1:] + entrada[0]
    print(entrada)

# 9 
entrada = input("Digite uma frase\n")
palavras = entrada.split()
for i in range(len(entrada)):
    palavras[0] = palavras[0][len(palavras):] + palavras[0]
    print(palavras)