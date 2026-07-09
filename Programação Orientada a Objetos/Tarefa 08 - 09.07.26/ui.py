from service import Service

class UI:
    @staticmethod
    def main():
        op = 0
        sub_op = 0
        while op != 4:
            op = UI.menu(op)
            sub_op = 0
            if op == 1: 
                while sub_op != 6:
                    sub_op = UI.menu(op)
                    if sub_op == 1: UI.cliente_inserir()
                    if sub_op == 2: UI.cliente_listar()
                    if sub_op == 3: UI.cliente_pesquisar_nome()
                    if sub_op == 4: UI.cliente_atualizar()
                    if sub_op == 5: UI.cliente_excluir()
                op = 0
            elif op == 2:
                while sub_op != 6:
                    sub_op = UI.menu(op)
                    if sub_op == 1: UI.servico_inserir() 
                    if sub_op == 2: UI.servico_listar()
                    if sub_op == 3: UI.servico_listar_descricao()
                    if sub_op == 4: UI.servico_atualizar()
                    if sub_op == 5: UI.servico_excluir
                op = 0
            elif op == 3:
                while sub_op != 7:
                    sub_op = UI.menu(op)
                    if sub_op == 1: UI.profissional_inserir()
                    if sub_op == 2: UI.profissional_listar()
                    if sub_op == 3: UI.profissional_pesquisar_id()
                    if sub_op == 4: UI.profissional_pesquisar_nome()
                    if sub_op == 5: UI.profissional_atualizar()
                    if sub_op == 6: UI.profissional_excluir()
                op = 0

    @staticmethod
    def menu(v):
        if v == 0: print("1- Cliente \n2- Serviço \n3- Profissional")
        elif v == 1: print("1- Inserir Cliente \n2- Listar Cliente \n3- Pesquisar por Nome \n4- Atualizar Cliente \n5- Excluir Cliente \n6- Sair")
        elif v == 2: print("1- Inserir Serviço \n2- Listar Serviço \n3- Listar por Descrição \n4- Atualizar Serviço \n5- Excluir Serviço \n6- Sair")
        elif v == 3: print("1- Inserir Profissional \n2- Listar Profissional \n3- Pesquisar por ID \n4- Pesquisar por Nome \n5- Atualizar Profissional \n6- Excluir Profissional")
        return int(input("Informe uma opção: "))
    @staticmethod
    def cliente_inserir():
        nome = input("Informe o nome: ")
        email = input("Informe o email: ")
        telefone = input("Informe o telefone: ")
        senha = input("Informe a senha: ")
        Service.cliente_inserir(nome, email, telefone, senha)
    @staticmethod
    def cliente_listar():
        for obj in Service.cliente_listar(): print(obj)
    @staticmethod
    def cliente_pesquisar_nome():
        nome = input("Informe o início do nome: ")
        for obj in Service.cliente_listar_nome(nome):
            print(obj)
    @staticmethod
    def cliente_atualizar():
        for obj in Service.cliente_listar: print(obj)
        id = int(input("Informe o ID: "))
        nome = input("Informe o nome: ")
        email = input("Informe o email: ")
        telefone = input("Informe o telefone: ")
        senha = input("Informe a senha: ")
        Service.cliente_atualizar(id, nome, email, telefone, senha)
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
    def servico_listar_descricao():
        descricao = input("Informe o início da descrição: ")
        for obj in Service.servico_listar_descricao(descricao): print(obj)
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

    @staticmethod
    def profissional_inserir():
        nome = input("Informe o nome: ")
        email = input("Informe o email: ")
        senha = input("Informe a senha: ")
        especialidade = input("Informe a especialidade: ")
        Service.profissional_inserir(nome, email, senha, especialidade)
    @staticmethod
    def profissional_listar():
        for obj in Service.profissional_listar(): print(obj)
    @staticmethod
    def profissional_pesquisar_id():
        id = int(input("Informe o início da id: "))
        for obj in Service.profissional_listar_id(id): print(obj)
    @staticmethod
    def profissional_pesquisar_nome():
        nome = input("Informe as iniciais do nome: ")
        for obj in Service.profissional_listar_nome(nome):
            print(obj)
    @staticmethod
    def profissional_atualizar():
        for obj in Service.profissional_listar: print(obj)
        id = int(input("Informe o ID: "))
        nome = input("Informe o nome: ")
        email = input("Informe o email: ")
        senha = input("Informe a senha: ")
        especialidade = input("Informe a especialidade: ")
        Service.profissional_atualizar(id, nome, email, senha, especialidade)
    @staticmethod
    def profissional_excluir():
        for obj in Service.profissional_listar(): print(obj)
        id = int(input("Informe o ID do profissional a ser excluído: "))
        Service.profissional_excluir(id)
UI.main()