from service import Service
from datetime import datetime

class UI:
    @staticmethod
    def main():
        op = 0
        while op != 13:
            op = UI.menu()
            if op == 1: UI.cliente_inserir()
            if op == 2: UI.cliente_listar()
            if op == 3: UI.cliente_atualizar()
            if op == 4: UI.cliente_excluir()
            if op == 5: UI.servico_inserir()
            if op == 6: UI.servico_listar()
            if op == 7: UI.servico_atualizar()
            if op == 8: UI.servico_excluir()
            if op == 9: UI.horario_inserir()
            if op == 10: UI.horario_listar()
            if op == 11: UI.horario_atualizar()
            if op == 12: UI.horario_excluir()

    @staticmethod
    def menu():
        print("----------- Cadastro de Clientes ----------")
        print("1-Inserir, 2-Listar, 3-Atualizar, 4-Excluir")
        print("----------- Cadastro de Serviços ----------")
        print("5-Inserir, 6-Listar, 7-Atualizar, 8-Excluir")
        print("----------- Cadastro de Horários ----------")
        print("9-Inserir, 10-Listar, 11-Atualizar, 12-Excluir")
        print("----------- Outras opções -----------------")
        print("13-Fim")
        return int(input("Informe uma opção: "))

    @staticmethod
    def cliente_inserir():
        #id = int(input("Informe o id: "))
        nome = input("Informe o nome: ")
        email = input("Informe o e-mail: ")
        fone = input("Informe o telefone: ")
        Service.cliente_inserir(nome, email, fone)

    @staticmethod
    def cliente_listar():
        for obj in Service.cliente_listar(): print(obj)

    @staticmethod
    def cliente_atualizar():
        for obj in Service().cliente_listar(): print(obj)
        id = int(input("Informe o id do cliente a ser atualizado: "))
        nome = input("Informe o novo nome: ")
        email = input("Informe o novo e-mail: ")
        fone = input("Informe o novo telefone: ")
        Service.cliente_atualizar(id, nome, email, fone)

    @staticmethod
    def cliente_excluir():
        for obj in Service().cliente_listar(): print(obj)
        id = int(input("Informe o id do cliente a ser excluído: "))
        Service.cliente_excluir(id)

    @staticmethod
    def servico_inserir():
        #id = int(input("Informe o id: "))
        descricao = input("Informe a descrição: ")
        valor = float(input("Informe o valor: "))
        Service.servico_inserir(descricao, valor)

    @staticmethod
    def servico_listar():
        for obj in Service.servico_listar(): print(obj)

    @staticmethod
    def servico_atualizar():
        for obj in Service.servico_listar(): print(obj)
        id = int(input("Informe o id do serviço a ser atualizado: "))
        descricao = input("Informe a nova descrição: ")
        valor = float(input("Informe o novo valor: "))
        Service.servico_atualizar(id, descricao, valor)

    @staticmethod
    def servico_excluir():
        for obj in Service.servico_listar(): print(obj)
        id = int(input("Informe o id do serviço a ser excluído: "))
        Service.servico_excluir(id)

    @staticmethod
    def horario_inserir():
        #id = int(input("Informe o id: "))
        data = datetime.strptime(input("Informe o horário: "), "%d/%m/%Y %H:%M")
        Service.horario_inserir(data)

    @staticmethod
    def horario_listar():
        for obj in Service.horario_listar(): print(obj)

    @staticmethod
    def horario_atualizar():
        for obj in Service.horario_listar(): print(obj)
        id = int(input("Informe o id do horário a ser atualizado: "))
        data = datetime.strptime(input("Informe o novo horário: "), "%d/%m/%Y %H:%M")
        Service.horario_atualizar(id, data)

    @staticmethod
    def horario_excluir():
        for obj in Service.horario_listar(): print(obj)
        id = int(input("Informe o id do horário a ser excluído: "))
        Service.horario_excluir(id)

UI.main()