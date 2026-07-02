import json
class Cliente:
    def __init__(self, id, nome, email,fone):
        self.set_id(id)
        self.set_nome(nome)
        self.set_email(email)
        self.set_fone(fone)
    def set_id(self, id):
        if id < 0: raise ValueError
        else: self.__id = id
    def get_id(self): return self.__id

    def set_nome(self, nome):
        if len(nome) == 0: raise ValueError
        else: self.__nome = nome
    def get_nome(self): return self.__nome

    def set_email(self, email):
        if len(email) == 0: raise ValueError
        else: self.__email = email
    def get_email(self): return self.__email

    def set_fone(self, fone):
        if len(fone) == 0: raise ValueError
        else: self.__fone = fone
    def get_email(self): return self.__fone

    def __str__(self):
        return f"{self.__id} - {self.__nome} - {self.__email} - {self.__fone}"
    
    def to_json(self): # Transforma em dict games
        return {"id": self.__id, "nome": self.__nome, "email": self.__email, "telefone": self.__fone}
    
    @staticmethod
    def from_json(dict):
        return Cliente(dict["id"], dict["nome"], dict["email"], dict["telefone"])

class ClienteUI:
    __objetos = []

    @staticmethod
    def main():
        op = 0
        while op != 8:
            op = ClienteUI.menu()
            if op == 1: ClienteUI.inserir()
            if op == 2: ClienteUI.listar()
            if op == 3: ClienteUI.listar_id()
            if op == 4: ClienteUI.atualizar()
            if op == 5: ClienteUI.excluir()
            if op == 6: ClienteUI.abrir()
            if op == 7: ClienteUI.salvar()

    @staticmethod
    def menu():
        print("1- Inserir \n2- Listar \n3- Listar por ID \n4- Atualizar \n5- Excluir \n6- Abrir \n7- Salvar \n8- Sair")
        return int(input("Escolha uma opção: "))
    
    @classmethod
    def inserir(cls):
        id = int(input("Digite o ID: "))
        nome = input("Digite o nome: ")
        email = input("Digite o email: ")
        fone = input("Digite o telefone: ")
        cls.__objetos.append(Cliente(id, nome, email, fone))

    @classmethod
    def listar(cls):
        for i in cls.__objetos: print(i)   
    
    @classmethod
    def listar_id(cls):
        id_selecionado = int(input("Digite o ID que deseja pesquisar: "))
        for i in cls.__objetos:
            if i.get_id() == id_selecionado: print(i)

    @classmethod
    def atualizar(cls):
        ClienteUI.listar()
        id_selecionado = int(input("Digite o ID que deseja pesquisar: "))
        for i in cls.__objetos:
            if i.get_id() == id_selecionado:
                cls.__objetos.remove(i)
                nome = input("Digite o nome: ")
                email = input("Digite o email: ")
                fone = input("Digite o telefone: ")
                cls.__objetos.append(Cliente(id_selecionado, nome, email, fone))
    
    @classmethod
    def excluir(cls):
        ClienteUI.listar()
        id_selecionado = int(input("Digite o ID que deseja pesquisar: "))
        for i in cls.__objetos:
            if i.get_id() == id_selecionado:
                cls.__objetos.remove(i)

    @classmethod
    def salvar(cls):    
        arquivo = open("clientes.json", mode = "w")
        json.dump(cls.__objetos, arquivo, default = Cliente.to_json, indent = 2)
        arquivo.close()

    @classmethod
    def abrir(cls):  
        try:  
            arquivo = open("clientes.json", mode = "r")
            list_dic = json.load(arquivo)
            arquivo.close()
            cls.__objetos = []
            for dic in list_dic:
                x = Cliente.from_json(dic)
                cls.__objetos.append(x)
        except FileNotFoundError:
            pass

ClienteUI.main()