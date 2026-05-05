class Viagem:
    def __init__(self, dest, dist, lt):
        self.set_destino(dest)
        self.set_distancia(dist)
        self.set_litros(lt)

    def set_destino(self, dest):
        if len(dest) > 0: self.__destino = dest
        else: raise ValueError
    def get_destino(self):
        return self.__destino

    def set_distancia(self, dist):
        if dist > 0: self.__distancia = dist
        else: raise ValueError
    def get_distancia(self):
        return self.__distancia

    def set_litros(self, lt):
        if lt > 0: self.__litros = lt
        else: raise ValueError
    def get_litros(self):
        return self.__litros
        
    def consumo(self):
        comb_consumido = round((self.__distancia/self.__litros),2)
        return comb_consumido

    def __str__(self):
        return f"Sua viagem de {self.__distancia}kms, com destino de {self.__destino}, que consumiu {self.__litros} litros de combustível. Essa viagem teve consumo médio de {self.consumo()}L por km rodado"

class Pais:
    def __init__(self, n, p, a):
        self.set_nome(n)
        self.set_populacao(p)
        self.set_area(a)

    def set_nome(self, n):
        if len(n) > 0: self.__nome = n
        else: raise ValueError
    def get_nome(self):
        return self.__nome

    def set_populacao(self, p):
        if p > 0: self.__populacao = p
        else: raise ValueError
    def get_populacao(self):
        return self.__populacao

    def set_area(self, a):
        if a > 0: self.__area = a
        else: raise ValueError
    def get_area(self):
        return self.__area

    def densidade(self):
        dens_demo = round((self.__populacao/self.__area),2)
        return dens_demo

    def __str__(self):
        return f"A densidade demográfica do(a) {self.__nome}, com população de {self.__populacao} habitantes e área de {self.__area}km², é de {self.densidade()}hab/km²"

class UI:
    @staticmethod
    def main():
        op = 0
        while op != 3:
            op = UI.menu()
            if op == 1: UI.calculo_viagem()
            if op == 2: UI.calculo_pais()

    @staticmethod
    def menu():
        print("1- Viagem \n2- País \n3- Fim")
        op = int(input("Informe a sua escolha: "))
        return op

    @staticmethod
    def calculo_viagem():
        dest = input("Digite o nome do destino de sua viagem: ")
        dist = float(input("Digite a distância percorrida em sua viagem (em kms): "))
        lt = float(input("Digite quantos litros de combustível foram gastos em sua viagem (em Ls): "))
        print(Viagem(dest, dist, lt))
    
    @staticmethod
    def calculo_pais():
        n = input("Digite o nome do país: ")
        p = int(input("Digite a população do seu país: "))
        a = float(input("Digite a área do seu país: "))
        print(Pais(n, p, a))

UI.main()