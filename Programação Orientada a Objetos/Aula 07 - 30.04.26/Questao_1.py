from random import randint

class Bingo:
    def __init__(self, nB):
        self.__bolas = []
        self.set_num_bolas(nB)

    def set_num_bolas(self, nB):
        if nB <= 0: raise ValueError
        else: self.__num_bolas = nB

    def sortear(self):
        if self.__num_bolas < 1: return -1
        else: return randint(1, self.__num_bolas)

    def verificador(self, bola_sorteada):
        if bola_sorteada in self.__bolas: self.sortear()
        elif bola_sorteada == -1: self.zerar()
        else: self.sorteados(bola_sorteada)

    def sorteados(self, b):
        self.__bolas.append(b)

    def zerar(self):
        self.__bolas = []
        self.set_num_bolas(int(input("Digite quantas bolas você quer que tenham disponíveis nesse bingo: ")))

class BingoUI:
    @staticmethod
    def main():
            op = 0
            while op != 4:
                op = BingoUI.menu()
                if op == 1: BingoUI.iniciar()
                if op == 2: BingoUI.sortear()
                if op == 3: BingoUI.verificar()
    @staticmethod
    def menu():
        print("1- Iniciar um novo jogo \n2- Sorter um número \n3- Verificar os números sorteados \n4- Sair")
        return int(input("Escolha um opção: "))

    @staticmethod
    def iniciar():
        

    @staticmethod
    def sortear():
        Bingo.verificador(sortear())
    @staticmethod
    def verificar():
