from datetime import datetime

class Paciente:
    def __init__(self, id, nome, cpf, telefone, nascimento):
        self.set_id(id)
        self.set_nome(nome)
        self.set_cpf(cpf)
        self.set_telefone(telefone)
        self.set_nascimento(nascimento)
    def set_id(self, id):
        if id < 0: raise ValueError()
        else: self.__id = id
    def get_id(self): return self.__id
    def set_nome(self, nome):
        if len(nome) == 0: raise ValueError()
        else: self.__nome = nome
    def get_nome(self): return self.__nome
    def set_cpf(self, cpf):
        if len(cpf) == 0: raise ValueError()
        else: self.__cpf = cpf
    def get_cpf(self): return self.__cpf
    def set_telefone(self, telefone):
        if len(telefone) == 0: raise ValueError()
        else: self.__telefone = telefone
    def get_telefone(self): return self.__telefone
    def set_nascimento(self, nascimento):
        if nascimento > datetime.now(): raise ValueError()
        else: self.__nascimento = nascimento
    def get_nascimento(self): return self.__nascimento
    def __str__(self):
        return f"{self.__id} - {self.__nome} - {self.__cpf} - {self.__telefone} - {self.__nascimento.strftime("%d/%m/%Y")}"
    def idade(self):
        tempo = datetime.now() - self.__nascimento
        anos = tempo.days // 365
        meses = tempo.days % 365 // 30
        return f"Idade: {anos} ano(s) e {meses} mes(es)"
    
class PacienteUI:
    __pacientes = []
    
    @staticmethod
    def main():
        op = 0
        while op != 7:
            op = PacienteUI.menu()
            if op == 1: PacienteUI.inserir()
            if op == 2: PacienteUI.listar()
            if op == 3: PacienteUI.atualizar()
            if op == 4: PacienteUI.excluir()
            if op == 5: PacienteUI.pesquisar()
            if op == 6: PacienteUI.aniversariantes()

    @staticmethod
    def menu():
        print("1-Inserir \n2-Listar \n3-Atualizar \n4-Excluir \n5-Pesquisar \n6-Aniversariantes \n7-Sair")
        return int(input("Escolha uma opção: "))
    
    @classmethod
    def inserir(cls):
        id = int(input("Informe o id: "))
        nome = input("Informe o nome: ")
        cpf = input("Informe o CPF: ")
        telefone = input("Informe o número de telefone: ")
        nascimento = datetime.strptime(input("Informe a data de nascimento: "), "%d/%m/%Y")
        x = Paciente(id, nome, cpf, telefone, nascimento)
        cls.__pacientes.append(x)

    @classmethod
    def listar(cls):
        if len(cls.__pacientes) == 0: print("Nenhum paciente cadastrado")
        else: 
            for x in cls.__pacientes: print(x)
    
    @classmethod
    def atualizar(cls):
        cls.listar()
        id = int(input("Informe o ID: "))
        x = cls.pesquisar(id)
        if x != None:
            cls.__pacientes.remove(x)
            nome = input("Novo nome: ")
            cpf = input("Novo CPF: ")
            telefone = input("Novo telefone: ")
            nascimento = datetime.strptime(input("Novo telefone: "), "%d/%m/%Y")
            novo = Paciente(id, nome, cpf, telefone, nascimento)
            cls.__pacientes.append(novo)
        else: raise NameError()
    
    @classmethod
    def excluir(cls):
        cls.listar()
        id = int(input("Informe o ID: "))
        x = cls.pesquisar(id)
        if x != None: cls.__pacientes.remove(x)

    @classmethod
    def pesquisar(cls):
        if len(cls.__pacientes) == 0: print("Nenhum paciente cadastrado")
        else:
            nome = input("Informe as iniciais do nome: ")
            for i in cls.__pacientes:
                if i.get_nome().startswith(nome):
                    print(i)
    
    @classmethod
    def aniversariantes(cls):
        if len(cls.__pacientes) == 0: print("Nenhum paciente cadastrado")
        mes = int(input("Informe o mês que deseja verificar os aniversariantes: "))
        for i in cls.__pacientes:
            if i.get_nascimento().month() == mes:
                print(i)
                
PacienteUI.main()
