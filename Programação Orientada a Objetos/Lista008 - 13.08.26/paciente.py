from datetime import datetime

class Paciente:
    def __init__(self, nome, cpf, telefone, nascimento):
        self.set_nome(nome)
        self.set_cpf(cpf)
        self.set_telefone(telefone)
        self.set_nascimento(nascimento)
    def set_nome(self, nome):
        if len(nome) == 0: raise ValueError
        self.__nome = nome
    def get_nome(self): return self.__nome
    def set_cpf(self, cpf):
        if len(cpf) == 0: raise ValueError
        self.__cpf = cpf
    def get_cpf(self): return self.__cpf
    def set_telefone(self, telefone):
        if len(telefone) == 0: raise ValueError
        self.__telefone = telefone
    def get_telefone(self): return self.__telefone
    def set_nascimento(self, nascimento):
        dt_nascimento = datetime.strptime(nascimento, "%d/%m/%Y")
        if dt_nascimento > datetime.now(): raise ValueError
        self.__nascimento = dt_nascimento
    def get_nascimento(self): return self.__nascimento
    def Idade(self):
        self.__idade = datetime.now() - self.__nascimento
        return f"A idade do paciente é de: {self.__idade.days // 365} anos e {(self.__idade.days % 365) // 30} meses"
    def __str__(self): return f"{self.__nome} - {self.__cpf} - {self.__telefone} - {self.__nascimento.strftime("%d/%m/%Y")}"