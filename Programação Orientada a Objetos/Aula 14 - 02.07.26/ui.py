from service import Service

class UI:
    @staticmethod
    def main():
        op = 0
        while op != 9:
            op = UI.menu()
            if op == 1: UI.cliente_inserir()
            if op == 2: UI.cliente_listar()
            if op == 3: UI.cliente_atualizar()
            if op == 4: UI.cliente_excluir()
    @staticmethod
    def menu():
        print("1- Inserir \n2- Listar \n3- Atualizar \n4- Excluir")
        return int(input("Informe uma opção: "))
    @staticmethod
    def cliente_inserir():
        id = int(input("Informe o ID: "))
        nome = input("Informe o nome: ")
        email = input("Informe o email: ")
        telefone = input("Informe o telefone: ")
        Service.cliente_inserir(id, nome, email, telefone)
    @staticmethod
    def cliente_listar():
        for obj in Service.cliente_listar(): print(obj)
    @staticmethod
    def cliente_atualizar():
        for obj in Service.cliente_listar: print(obj)
        id = int(input("Informe o ID: "))
        nome = input("Informe o nome: ")
        email = input("Informe o email: ")
        telefone = input("Informe o telefone: ")
        Service.cliente_atualizar(id, nome, email, telefone)
    @staticmethod
    def cliente_excluir():
        for obj in Service.cliente_listar(): print(obj)
        id = int(input("Informe o ID do cliente a ser escolhido: "))
        Service.cliente_excluir(id)
UI.main()