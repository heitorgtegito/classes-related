# Questão 01
print("Digite dois valores inteiros")
n1 = int(input())
n2 = int(input())
if n1 > n2: 
    maior = n1
elif n1 < n2: 
    maior = n2
else: print("Os dois números são iguais")

# Questão 2
entrada = input("Digite dois valores inteiros separados por um operador +, -, * ou /\n")
a = 0
for i in entrada:
    if i == '+': 
        operacao = "soma"
        break
    elif i == '-': 
        operacao = "subtracao"
        break
    elif i == '*': 
        operacao = "multiplicacao"
        break
    elif i == '/': 
        operacao = "divisao"
        break
    a += 1
n1 = int(entrada[:a])
n2 = int(entrada[a:])
match operacao:
    case "soma": resultado = n1 + n2
    case "subtracao": resultado = n1 - n2
    case "multiplicacao": resultado = n1 * n2
    case "divisao": resultado = n1 / n2
print(f"O resultado é {resultado}")

# Questão 3
entrada = input("Digite uma frase:\n")
soma = 0
for i in "0123456789":
    if i in entrada:
        numero = int(i)
        soma += numero
print(soma)

# Questão 4 --> Dá pra usar o mesmo código da passada
entrada = input("Digite uma sequência de números separados por vírgula:\n")
soma = 0
for i in "0123456789":
    if i in entrada:
        numero = int(i)
        soma += numero
print(soma)

# Questão 5
class País:
    def __init__(self):
        self.nome = ''
        self.populacao = 0
        self.area = 0
    def densidade_demografica(self):
        return print(f'A densidade demográfica do {self.nome} é de {(self.populacao/self.area):.2f} hab/km2')
x = País()
x.nome = input("Digite o nome do país: ")
x.populacao = int(input("Digite sua população: "))
x.area = int(input("Digite a área em km2: "))
x.densidade_demografica()