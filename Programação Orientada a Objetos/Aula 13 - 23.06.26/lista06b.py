import json
from datetime import datetime

class Contato:
    def __init__(self, id, nome, email, fone, nascimento):
        self.set_id(id)
        self.set_nome(nome)
        self.set_email(email)
        self.set_fone(fone)
        self.set_nascimento(nascimento)
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

    def set_nascimento(self, nascimento):
        if nascimento > datetime.now(): raise ValueError
        else: self.__nascimento = nascimento
    def get_nascimento(self): return self.__nascimento

    def __str__(self):
        return f"{self.__id} - {self.__nome} - {self.__email} - {self.__fone} - {self.__nascimento.strftime("%d/%m/%Y")}"
    
    def to_json(self):
        return {"id": self.__id, "nome": self.__nome, "email": self.__email, "telefone": self.__fone, "nascimento": self.__nascimento.strftime("%d/%m/%Y")}
    
    @staticmethod
    def from_json(dict):
        return Contato(dict["id"], dict["nome"], dict["email"], dict["telefone"], datetime.strptime(dict["nascimento"], "%d/%m/%Y"))

class ContatoUI:
    __contatos = []

    @staticmethod
    def main():
        op = 0
        while op != 10:
            op = ContatoUI.menu()
            if op == 1: ContatoUI.inserir()
            if op == 2: ContatoUI.listar()
            if op == 3: ContatoUI.listar_id()
            if op == 4: ContatoUI.atualizar()
            if op == 5: ContatoUI.excluir()
            if op == 6: ContatoUI.pesquisar()
            if op == 7: ContatoUI.aniversariantes()
            if op == 8: ContatoUI.salvar()
            if op == 9: ContatoUI.abrir()

    @staticmethod
    def menu():
        print("1- Inserir \n2- Listar \n3- Listar por ID \n4- Atualizar \n5- Excluir \n6- Pesquisar \n7- Aniversariantes  \n8- Salvar \n9- Abrir \n10- Sair")
        return int(input("Escolha uma opção: "))
    
    @classmethod
    def inserir(cls):
        id = int(input("Digite o ID: "))
        nome = input("Digite o nome: ")
        email = input("Digite o email: ")
        fone = input("Digite o telefone: ")
        nascimento = datetime.strptime(input("Data de Nascimento (ex.: 27/11/2009): "), "%d/%m/%Y")
        cls.__contatos.append(Contato(id, nome, email, fone, nascimento))

    @classmethod
    def listar(cls):
        for i in cls.__contatos: print(i)   
    
    @classmethod
    def listar_id(cls):
        id_selecionado = int(input("Digite o ID que deseja pesquisar: "))
        for i in cls.__contatos:
            if i.get_id() == id_selecionado: print(i)

    @classmethod
    def atualizar(cls):
        ContatoUI.listar()
        id_selecionado = int(input("Digite o ID que deseja pesquisar: "))
        for i in cls.__contatos:
            if i.get_id() == id_selecionado:
                cls.__contatos.remove(i)
                nome = input("Digite o nome: ")
                email = input("Digite o email: ")
                fone = input("Digite o telefone: ")
                nascimento = datetime.strptime(input("Data de Nascimento (ex.: 27/11/2009): "), "%d/%m/%Y")
                cls.__contatos.append(Contato(id_selecionado, nome, email, fone, nascimento))
    
    @classmethod
    def excluir(cls):
        ContatoUI.listar()
        id_selecionado = int(input("Digite o ID que deseja pesquisar: "))
        for i in cls.__contatos:
            if i.get_id() == id_selecionado:
                cls.__contatos.remove(i)

    @classmethod
    def pesquisar(cls):
        if len(cls.__contatos) == 0: print("Nenhum contato cadastrado")
        else:
            nome = input("Informe as iniciais do nome: ")
            for i in cls.__contatos:
                if i.get_nome().startswith(nome):
                    print(i)
    
    @classmethod
    def aniversariantes(cls):
        m = int(input("Informe o mês para a lista de aniversariantes (1-12): "))
        for x in cls.__contatos:
            if x.get_nascimento().month == m: print(x)

    @classmethod
    def salvar(cls):    
        arquivo = open("contatos.json", mode = "w")
        json.dump(cls.__contatos, arquivo, default = Contato.to_json, indent = 2)
        arquivo.close()

    @classmethod
    def abrir(cls):  
        try:  
            arquivo = open("contatos.json", mode = "r")
            list_dic = json.load(arquivo)
            arquivo.close()
            cls.__contatos = []
            for dic in list_dic:
                x = Contato.from_json(dic)
                cls.__contatos.append(x)
        except FileNotFoundError:
            pass

ContatoUI.main()