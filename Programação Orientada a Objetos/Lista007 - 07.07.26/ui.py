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
            if op == 5: UI.servico_inserir() 
            if op == 6: UI.servico_listar()
            if op == 7: UI.servico_atualizar()
            if op == 8: UI.servico_excluir
    @staticmethod
    def menu():
        print("1- Inserir Cliente \n2- Listar Cliente \n3- Atualizar Cliente \n4- Excluir Cliente \n5- Inserir Serviço \n6- Listar Serviço \n7- Atualizar Serviço \n8- Excluir Serviço \n9- Sair")
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
        id = int(input("Informe o ID do cliente a ser excluído: "))
        Service.cliente_excluir(id)
    @staticmethod
    def servico_inserir():
        id = int(input("Informe o ID: "))
        descricao = input("Informe a descrição: ")
        valor = float(input("Informe o valor: "))
        Service.servico_inserir(id, descricao, valor)
    @staticmethod
    def servico_listar():
        for obj in Service.servico_listar(): print(obj)
    @staticmethod
    def servico_atualizar():
        for obj in Service.servico_listar: print(obj)
        id = int(input("Informe o ID: "))
        descricao = input("Informe a descrição: ")
        valor = float(input("Informe o valor: "))
        Service.servico_atualizar(id, descricao, valor)
    @staticmethod
    def servico_excluir():
        for obj in Service.servico_listar(): print(obj)
        id = int(input("Informe o ID do serviço a ser excluído: "))
        Service.servico_excluir(id)
UI.main()