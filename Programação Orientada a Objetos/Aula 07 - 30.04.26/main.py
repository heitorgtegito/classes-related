# class Bingo:
#     def __init__(self, nB, b):
#         self.set_num_bolas(nB)
#         self.set_bolas(b)
#     def set_num_bolas(self, nB):
#         if nB <= 0: raise ValueError
#         else: self.__num_bolas = nB
#     def set_bolas(self, b):
#         if b <= 0: raise ValueError
#         else: self.__bolas = b
#     def sortear(self):

#     def sorteados(self):

class Contato:
    def __init__(self, id, nome, email, fone):
        self.set_email(email)
        self.set_fone(fone)
        self.set_nome(nome)
        self.set_id(id)
    def set_email(self, email):
        self.__email = email
    def set_fone(self, fone):
        self.__fone = fone
    def set_id(self, id):
        if id < 0: raise ValueError
        else: self.__id = id
    def set_nome(self, nome):
        if len(nome) == 0: raise ValueError
        else: self.__nome = nome
    def get_id(self): return self.__id
    def get_nome(self): return self.__nome
    def get_email(self): return self.__email
    def get_fone(self): return self.__fone
    def __str__(self) -> str:
        return f"{self.__id} - {self.__nome} - {self.__email} - {self.__fone}"

class ContatoUI:
    contatos = []
    @staticmethod
    def main():
        op = 0
        while op != 6:
            op = ContatoUI.menu()
            if op == 1: ContatoUI.inserir()
            if op == 2: ContatoUI.listar()
            if op == 3: ContatoUI.atualizar()
            if op == 4: ContatoUI.excluir()
            if op == 5: ContatoUI.pesquisar()
 
    @staticmethod
    def menu():
        print("1-Inserir \n2- Listar \n3- Atualizar \n4- Excluir \n5- Pesquisar \n6- Fim")
        return int(input("Escolha uma opção: "))
 
    @classmethod
    def inserir(cls):
        id = int(input("Informe o ID do contato: "))
        nome = input("Informe o nome: ")
        email = input("Informe o email: ")
        fone = input("Informe o telefone: ")
        x = Contato(id, nome, email, fone)
        cls.contatos.append(x)
        print("Contato inserido com sucesso!")
    @classmethod
    def listar(cls):
        if len(cls.contatos) == 0: print("Nenhum contato na Agenda")
        else: 
            for x in cls.contatos: print(x)
    @classmethod
    def atualizar(cls):
        for x in cls.contatos: print(x)
        mudar_id = int(input("Informe o ID do contato que deseja mudar as informações: "))
        novo_nome = input("Informe o novo nome: ")
        novo_email = input("Informe o novo email: ")
        novo_fone = input("Informe o novo telefone: ")
        x = Contato(mudar_id, novo_nome, novo_email, novo_fone)
        for i in cls.contatos:
            cls.contatos[i].split('-')

        
    @classmethod
    def excluir(cls):
        for x in cls.contatos: print(x)
        excluir_id = int(input("Informe o ID do contato que deseja mudar as informações: "))
    @classmethod
    def pesquisar(cls):
        for blabla in range(1, 10):
            print("LA")
            
ContatoUI.main()