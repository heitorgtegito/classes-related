class Triangulo:
    def __init__(self):
        self.__base = 0
        self.__altura = 0
    def set_base(self):
        base = int(input("Digite a base do triângulo: \n"))
        if base <= 0: raise ValueError()
        else: self.__base = base
        return self.__base
    def set_altura(self):
        altura = int(input("Digite a altura do triângulo: \n"))
        if altura <= 0: raise ValueError()
        else: self.__altura = altura
        return self.__altura
    def get_base(self):
        return self.__base
    def get_altura(self):
        return self.__altura
    def hipotenusa(self):
        return (self.__base**2 + self.__altura**2)**0.5
    def perimetro(self):
        return self.__base + self.__altura + ((self.__base**2 + self.__altura**2)**0.5)
    def area(self):
        return (self.__base*self.__altura)/2

class Circulo:
    def __init__(self):
        self.__raio = 0
    def set_raio(self, v):
        if v >= 0: self.__raio = v
        else: raise ValueError()
    def get_raio(self):
        return self.__raio
    def calc_area(self):
        return 3.14 * (self.__raio **2)
    def calc_circunferencia(self):
        return 2 * 3.14 * self._raio

class Viagem:
    def __init__(self):
        self.__distancia = 0
        self.__tempo = 0
        self.__horas = 0
        self.__minutos = 0
    def set_distancia(self, d):
        if d >= 0: self.__distancia = d
        else: raise ValueError()
    def set_tempo(self, h, m):
        tempo_conta = h + (1*m/60)
        self.__horas = h
        self.__minutos = m
        if h >= 0 and m >= 0: self.__tempo = tempo_conta
        else: raise ValueError()
    def get_distancia(self):
        return self.__distancia
    def get_tempo(self):
        return self.__tempo
    def get_horas_e_minutos(self):
        return self.__horas, self.__minutos
    def velocidade_media(self):
        return self.__distancia/self.__tempo
    
class Conta_Bancaria:
    def __init__(self):
        self.__titular = ""
        self.__nconta = 0
        self.__saldo = 0
        self.__backup = None
    def def_infos(self):
        titular = input("Digite o nome do titular da conta: ")
        nconta = int(input("Digite o número da conta: "))
        saldo = float(input("Digite o saldo da conta: "))
        if nconta < 0: raise ValueError()
        else: 
            self.__titular = titular 
            self.__nconta = nconta
            self.__saldo = saldo
        self.backup()
    def get_infos(self):
        return self.__titular, self.__nconta, self.__saldo
    def backup(self):
        self.__backup = (self.__titular, self.__nconta, self.__saldo)
    def get_backup(self):
        return self.__backup
    def restaurar(self):
        infos = self.get_backup()
        self.__titular = infos[0]
        self.__nconta = infos[1]
        self.__saldo = infos[2]
        print("Informações restauradas!")
    def deposito(self):
        valor_deposito = float(input(f'Seu saldo atual é: R${self.__saldo}, quanto você quer depositar?\n'))
        if valor_deposito <= 0: raise ValueError("Valor inválido para depósito")
        else: self.__saldo += valor_deposito
        print(f'Seu saldo agora é de: R${self.__saldo}')
    def saque(self):
        valor_saque = float(input(f'Seu saldo atual é: R${self.__saldo}, quanto você quer sacar?\n'))
        if valor_saque > self.__saldo: raise ValueError("Você não possui saldo suficiente para sacar essa quantia.")
        elif valor_saque <= 0: raise ValueError("Valor inválido para saque")
        else: self.__saldo -= valor_saque
        print(f'Seu saldo agora é de: R${self.__saldo}')

class Ingresso:
    def __init__(self):
        self.__sessao = None
        self.__valores = None
        self.__backup = None
    def sessao():
        d = int(input("Qual o dia da semana que você deseja? \n1- Segunda-Feira \n2- Terça-Feira \n3- Quarta-Feira \n4-Quinta-Feira \n5-Sexta-Feira \n6- Sábado \n7- Domingo"))
        match d:
            case 1: dia = "Segunda-Feira"
            case 2: dia = "Terça-Feira"
            case 3: dia = "Quarta-Feira"
            case 4: dia = "Quinta-Feira"
            case 5: dia = "Sexta-Feira"
            case 6: dia = "Sábado"
            case 7: dia = "Domingo"
            case _ : raise ValueError()
        h = input("Qual o horário da sessão? -- Digite no seguinte formato: XX:XX\n")
        h = h.split(":")
        horas = int(h[0])
        minutos = int(h[1])
        # Transformar esses minutos em decimais pra conseguir checar se o horário tá entre as 17h-00h pra aumentar o preço em 50%. Depois é só ir pros valores e fazer o backup/restauração
    def valores():



class UI:
    @staticmethod
    def main():
        op = 0
        while op != 9:
            op = UI.menu()
            if op == 1: UI.triangulo()
            if op == 2: UI.circulo()
            if op == 3: UI.viagem()
            if op == 4: UI.conta_bancaria()
            if op == 5: UI.ingresso()

    @staticmethod
    def menu():
        print("1-Triângulo \n2-Círculo \n3-Viagem \n4-Conta Bancária \n5-Ingresso \n9-Fim")
        op = int(input("Informe uma opção: "))
        return op

    @staticmethod
    def triangulo():
        x = Triangulo()
        x.set_base()
        x.set_altura()
        op_t = int(input("Qual a informação que deseja saber? \n1- A hipotenusa do triângulo \n2- O perímetro do triângulo \n3- A área do triângulo \n4- Sair do menu de triângulo \n"))
        if op_t == 1: print(f'\nA hipotenusa do seu triângulo de base {x.get_base()} e altura {x.get_altura()} é {x.hipotenusa()}\n')
        if op_t == 2: print(f'\nO perímetro do seu triângulo de base {x.get_base()} e altura {x.get_altura()} é {x.perimetro()}\n')
        if op_t == 3: print(f'\nA área do seu triângulo de base {x.get_base()} e altura {x.get_altura()} é {x.area()}\n')
        if op_t == 4: UI.main()

    @staticmethod
    def circulo():
        x = Circulo()
        x.set_raio(float(input("Digite o valor do raio:\n")))
        op_c = int(input("Qual a informação que deseja saber? \n1- A hipotenusa do círculo \n2- O perímetro do círculo \n3- Sair do menu de círculo \n"))
        if op_c == 1: print(f'\nA área do seu círculo de raio {x.get_raio()} é {x.calc_area()}\n')
        if op_c == 2: print(f'\nO perímetro do seu círculo de raio {x.get_raio()} é {x.calc_circunferencia()}\n')
        if op_c == 3: UI.main()

    @staticmethod
    def viagem():
        x = Viagem()
        x.set_distancia(float(input("Digite a distância da viagem:\n")))
        x.set_tempo(int(input("Digite quantas horas a viagem demorou:\n")), int(input("Digite quantos minutos a viagem demorou:\n")) )
        print(f'\nEm sua viagem de {x.get_horas_e_minutos()[0]} horas e {x.get_horas_e_minutos()[1]} minutos, com distância de {x.get_distancia()} km, sua velocidade média foi de {x.velocidade_media()}km/h\n')
    
    @staticmethod
    def conta_bancaria():
        x = Conta_Bancaria()
        x.def_infos()
        op_cb = -1
        while op_cb != 0:
            op_cb = int(input("O que você deseja fazer? \n1- Ver minhas informações \n2- Depositar \n3- Sacar \n8- Restaurar minha conta \n9- Redefinir minhas informações \n0- Sair"))
            if op_cb == 1: print(f'Informações da Conta\nNome do titular: {x.get_infos()[0]}\nNúmero da conta: {x.get_infos()[1]}\nSaldo da conta: R${x.get_infos()[2]}')
            if op_cb == 2: x.deposito()
            if op_cb == 3: x.saque()
            if op_cb == 8: x.restaurar()
            if op_cb == 9: x.def_infos()

    @staticmethod
    def ingresso():
        x = Ingresso()

UI.main()
