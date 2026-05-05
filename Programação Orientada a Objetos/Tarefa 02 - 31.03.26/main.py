# Questão 01
class agua:
    def __init__(self):
        self.mes = 0
        self.ano = 0
        self.consumo = 0
    def calcular(self):
        if self.consumo <= 10:
            conta = 38.00
        elif 10 < self.consumo <= 20:
            valor_extra = self.consumo - 10
            conta = 38.00 + valor_extra * 5.00
        elif 20 < self.consumo:
            valor_extra = self.consumo - 20
            conta = 38.00 + 50.00 + valor_extra * 6
        return conta

x = agua()
x.ano = int(input("Digite qual o ano que você deseja registrar como parte da conta de água (Digite apenas o número referente ao ano)\n"))
x.mes = int(input("Digite qual o mês que você deseja ter a conta calculada (Digite apenas o número referente ao mês)\n"))
match x.mes:
    case 1 : mes = "Janeiro"
    case 2 : mes = "Fevereiro"
    case 3 : mes = "Março"
    case 4 : mes = "Abril"
    case 5 : mes = "Maio"
    case 6 : mes = "Junho"
    case 7 : mes = "Julho"
    case 8 : mes = "Agosto"
    case 9 : mes = "Setembro"
    case 10 : mes = "Outubro"
    case 11 : mes = "Novembro"
    case 12 : mes = "Dezembro"
x.consumo = int(input(f"Digite qual foi o consumo de água no mês de {mes} do ano de {x.ano} (Digite apenas o número referente ao consumo)\n"))
print(f"A sua conta de água no mês de {mes} do ano de {x.ano}, com consumo de {x.consumo}m3 foi de R${x.calcular()}")

# Questão 02
class País:
    def __init__(self):
        self.nome = ""
        self.populacao = 0
        self.area = 0
    def densidade_demografica(self):
        return round(self.populacao/self.area,2)
x = País()
dict = {}
for i in range(10):
    x.nome = input("Digite o nome do País\n")
    x.populacao = float(input("Digite a população do País\n"))
    x.area = float(input("Digite a área do País\n"))
    dict[x.nome] = x.densidade_demografica()
    maior = max(dict, key=dict.get)
print(f"O País com maior densidade demográfica dos que foram digitados é {maior}, com {dict[maior]}hab/km2")