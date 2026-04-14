from mimetypes import init


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
        self.__tempo = ""
    def set_distancia(self, d):
        if d >= 0: self.__distancia = d
        else: raise ValueError()
    def set_tempo(self, t):
        tem = t.split(".")
        horas = int(tem[0])
        minutos = int(tem[1])
        tempo = # Fi, bota isso daq pra transformar oq atualmente tá como 3 horas e 30 min pra virar 3.5h tlgd
        if minutos >= 0 and horas >= 0: self.__tempo = tempo
        else: raise ValueError()
    def get_distancia(self, d):
        return self.__distancia
    def get_tempo(self, t):
        return self.__tempo
    def velocidade_media(self):
        return self.__distancia/self.__tempo
    
class Conta_Bancaria:
    def __init__(self):
        self.__titular = ""
        self.__nconta = 0
        self.__saldo = 0
    def def_infos(self):
        titular = input("Digite o nome do titular da conta: ")
        nconta = int(input("Digite o número da conta: "))
        saldo = float(input("Digite o saldo da conta: "))


class UI:
    @staticmethod
    def main():
        op = 0
        while op != 9:
            op = UI.menu()
            if op == 1: UI.triangulo()
            if op == 2: UI.circulo()
    
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
        op_t = int(print("Qual a informação que deseja saber? \n1- A hipotenusa do triângulo \n2- O perímetro do triângulo \n3- A área do triângulo \n4- Sair do menu de triângulo \n"))
        while op_t != 4:
            if op_t == 1: print(f'A hipotenusa do seu triângulo de base {x.get_base()} e altura {x.get_altura()} é {x.hipotenusa()}')
            if op_t == 2: print(f'O perímetro do seu triângulo de base {x.get_base()} e altura {x.get_altura()} é {x.perimetro()}')
            if op_t == 3: print(f'A área do seu triângulo de base {x.get_base()} e altura {x.get_altura()} é {x.area()}')

    @staticmethod
    def circulo():
        x = Circulo()
        x.set_raio(float(input("Digite o valor do raio:\n")))
        op_c = int(print("Qual a informação que deseja saber? \n1- A hipotenusa do círculo \n2- O perímetro do círculo \n3- Sair do menu de círculo \n"))
        while op_c != 3:
            if op_c == 1: print(f'A área do seu círculo de raio {x.get_raio()} é {x.calc_area()}')
            if op_c == 2: print(f'O perímetro do seu círculo de raio {x.get_raio()} é {x.calc_circunferencia()}')
    
    @staticmethod
    def viagem():
        x = Viagem()
        x.set_distancia(float(input("Digite a distância da viagem:\n")))
        x.set_tempo(input("Digite o tempo da viagem:\n (Use o ponto final '.' para separar as horas dos minutos)"))
        print(f'Em sua viagem de {x.get_tempo()[0]} horas e {x.get_tempo()[1]} minutos, com distância de {x.get_distancia()} km, sua velocidade média foi de {x.velocidade_media()}')
    
    @staticmethod
    def conta_bancaria():
        x = Conta_Bancaria

UI()