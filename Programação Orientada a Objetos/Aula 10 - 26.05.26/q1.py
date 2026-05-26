from datetime import datetime, timedelta

class Treino:
    def __init__(self, id, data, distancia, tempo):
        self.set_id(id)
        self.set_data(data)
        self.set_distancia(distancia)
        self.set_tempo(tempo)
    def set_id(self, id):
        if id < 0: raise ValueError
        else: self.__id = id
    def get_id(self): return self.__id
    def set_data(self, data):
        if data > datetime.now(): raise ValueError
        else: self.__data = data
    def get_data(self): return self.__data
    def set_distancia(self, distancia):
        if distancia < 0: raise ValueError
        else: self.__distancia = distancia
    def get_distancia(self): return self.__distancia
    def set_tempo(self, tempo):
        if tempo < 0: raise ValueError
        else: self.__tempo = tempo
    def get_tempo(self): return self.__tempo
    def Pace(self):
        tempo = self.__tempo.total_seconds()
        distancia = self.__distancia
        pace = tempo / distancia
        return timedelta(seconds=pace)
    def __str__(self): return f"{self.__id} - {self.__data} - {self.__distancia} - {self.__tempo}"

class TreinoUI:
    __treinos = []
    @staticmethod
    def main():
        op = 0
        while op != 7:
            op = TreinoUI.menu()
            if op == 1: TreinoUI.inserir()
            if op == 2: TreinoUI.listar()
            if op == 3: TreinoUI.listar_id()
            if op == 4: TreinoUI.atualizar()
            if op == 5: TreinoUI.excluir()
            if op == 6: TreinoUI.maisrapido()

    @staticmethod
    def menu():
        print("1-Inserir \n2-Listar \n3-Listar ID \n4-Atualizar \n5-Excluir \n6-Mais Rápido \n7-Sair")
        return int(input("Escolha uma opção: "))
    
    @classmethod
    def inserir(cls):
        id = int(input("Informe o id: "))
        data = datetime.strptime(input("Informe a data do treino: "), "%d/%m/%Y")
        distancia = float(input("Informe a distância (no modelo KM.M): "))
        duracao = input("Informe o tempo (no modelo H:Min:Sec): ").split(":")
        tempo = timedelta(hours=int(duracao[0]), minutes=int(duracao[1]), seconds=int(duracao[2]))
        x = Treino(id, data, distancia, tempo)
        cls.__treinos.append(x)

    @classmethod
    def listar(cls):
        if len(cls.__treinos) == 0: print("Nenhum paciente cadastrado")
        else: 
            for x in cls.__treinos: print(x)
    
    @classmethod
    def listar_id(cls):
        if len(cls.__treinos) == 0: print("Nenhum paciente cadastrado")
        else:
            id = int(input("Informe o Id do treino: "))
            for i in cls.__treinos:
                if i.get_id() == id:
                    print(i)

    
    @classmethod
    def atualizar(cls):
        cls.listar()
        id = int(input("Informe o ID: "))
        x = cls.pesquisar(id)
        if x != None:
            cls.__treinos.remove(x)
            data = datetime.strptime(input("Informe a data do treino: "), "%d/%m/%Y")
            distancia = float(input("Informe a distância (no modelo KM.M): "))
            duracao = input("Informe o tempo (no modelo H:Min:Sec): ").split(":")
            tempo = timedelta(hours=int(duracao[0]), minutes=int(duracao[1]), seconds=int(duracao[2]))
            novo = Treino(id, data, distancia, tempo)
            cls.__treinos.append(novo)
        else: raise NameError()
    
    @classmethod
    def excluir(cls):
        cls.listar()
        id = int(input("Informe o ID: "))
        x = cls.pesquisar(id)
        if x != None: cls.__treinos.remove(x)

    @classmethod
    def maisrapido(cls):
        if len(cls.__treinos) == 0: print("Nenhum paciente cadastrado")
        else: print(min(cls.__treinos, key = lambda x : x.Pace()))

TreinoUI.main()