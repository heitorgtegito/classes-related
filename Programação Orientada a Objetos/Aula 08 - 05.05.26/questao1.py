class Time:
    def __init__(self, id, nome, estado):
        self.set_id(id)
        self.set_nome(nome)
        self.set_estado(estado)

    def set_id(self, id):
        if id <= 0: raise ValueError()
        else: self.__id = id
    def get_id(self): return self.__id
    
    def set_nome(self, nome):
        if len(nome) == 0 : raise ValueError()
        else: self.__nome = nome
    def get_nome(self): return self.__nome

    def set_estado(self, estado):
        if len(estado) == 0: raise ValueError()
        else: self.__estado = estado
    def get_estado(self): return self.__estado

    def __str__(self):
        return f"{self.__id} - {self.__nome} - {self.__estado}"


class Jogador:
    def __init__(self, id, nome, camisa, id_time):
        self.set_id(id)
        self.set_nome(nome)
        self.set_camisa(camisa)
        self.set_id_time(id_time)

    def set_id(self, id):
        if id < 0: raise ValueError()
        else: self.__id = id
    def get_id(self): return self.__id

    def set_nome(self, nome):
        if len(nome) == 0: raise ValueError()
        else: self.__nome = nome
    def get_nome(self): return self.__nome

    def set_camisa(self, camisa):
        if camisa <= 0: raise ValueError()
        else: self.__camisa = camisa
    def get_camisa(self): return self.__camisa

    def set_id_time(self, id_time):
        self.__id_time = id_time
    def get_id_time(self): return self.__id_time

    def __str__(self): return f"{self.__id} - {self.__nome} - Camisa {self.__camisa} - Time {self.__id_time}"


class UI:
    times = []
    jogadores = []

    @staticmethod
    def main():
        op = 0
        while op != 11:
            op = UI.menu()
            if op == 1: UI.inserir_time()
            if op == 2: UI.listar_times()
            if op == 3: UI.atualizar_time()
            if op == 4: UI.excluir_time()
            if op == 5: UI.inserir_jogador()
            if op == 6: UI.listar_jogadores()
            if op == 7: UI.atualizar_jogador()
            if op == 8: UI.excluir_jogador()
            if op == 9: UI.listar_jogadores_time()
            if op == 10: UI.transferir_jogador()

    @staticmethod
    def menu():
        print("1-Inserir Time \n2-Listar Times \n3-Atualizar Time \n4-Excluir Time \n5-Inserir Jogador \n6-Listar Jogadores \n7-Atualizar Jogador \n8-Excluir Jogador \n9-Listar Jogadores do Time \n10-Transferir Jogador \n11-Sair")
        return int(input("Escolha uma opção: "))

    @classmethod
    def inserir_time(cls):
        id = int(input("Id do time: "))
        nome = input("Nome do time: ")
        estado = input("Estado do time: ")
        x = Time(id, nome, estado)
        cls.times.append(x)
        print("Time cadastrado")

    @classmethod
    def listar_times(cls):
        if len(cls.times) == 0:
            print("Nenhum time cadastrado")
        else:
            for x in cls.times:
                print(x)

    @classmethod
    def procurar_time(cls, id):
        for x in cls.times:
            if x.get_id() == id:
                return x
        return None

    @classmethod
    def atualizar_time(cls):
        cls.listar_times()
        id = int(input("Informe o id do time: "))
        x = cls.procurar_time(id)
        if x != None:
            cls.times.remove(x)
            nome = input("Novo nome: ")
            estado = input("Novo estado: ")
            novo = Time(id, nome, estado)
            cls.times.append(novo)

    @classmethod
    def excluir_time(cls):
        cls.listar_times()
        id = int(input("Informe o id do time: "))
        x = cls.procurar_time(id)
        if x != None: cls.times.remove(x)

    @classmethod
    def inserir_jogador(cls):
        id = int(input("Id do jogador: "))
        nome = input("Nome do jogador: ")
        camisa = int(input("Número da camisa: "))
        id_time = int(input("Id do time: "))
        x = Jogador(id, nome, camisa, id_time)
        cls.jogadores.append(x)
        print("Jogador cadastrado")

    @classmethod
    def listar_jogadores(cls):
        if len(cls.jogadores) == 0:
            print("Nenhum jogador cadastrado")
        else:
            for x in cls.jogadores:
                print(x)

    @classmethod
    def procurar_jogador(cls, id):
        for x in cls.jogadores:
            if x.get_id() == id:
                return x
        return None

    @classmethod
    def atualizar_jogador(cls):
        cls.listar_jogadores()
        id = int(input("Informe o id do jogador: "))
        x = cls.procurar_jogador(id)
        if x != None:
            cls.jogadores.remove(x)
            nome = input("Novo nome: ")
            camisa = int(input("Nova camisa: "))
            id_time = int(input("Novo id do time: "))
            novo = Jogador(id, nome, camisa, id_time)
            cls.jogadores.append(novo)

    @classmethod
    def excluir_jogador(cls):
        cls.listar_jogadores()
        id = int(input("Informe o id do jogador: "))
        x = cls.procurar_jogador(id)
        if x != None: cls.jogadores.remove(x)

    @classmethod
    def listar_jogadores_time(cls):
        id_time = int(input("Informe o id do time: "))
        for x in cls.jogadores:
            if x.get_id_time() == id_time:
                print(x)

    @classmethod
    def transferir_jogador(cls):
        cls.listar_jogadores()
        id = int(input("Informe o id do jogador: "))
        x = cls.procurar_jogador(id)
        if x != None:
            novo_time = int(input("Novo id do time: "))
            x.set_id_time(novo_time)
            print("Jogador transferido")

UI.main()