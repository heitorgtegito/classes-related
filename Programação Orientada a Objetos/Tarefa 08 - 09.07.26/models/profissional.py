class Profissional:
    def __init__(self, id, nome, email, senha, especialidade):
        self.set_id(id)
        self.set_nome(nome)
        self.set_email(email)
        self.set_senha(senha)
        self.set_especialidade(especialidade)
    
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

    def set_senha(self, senha):
        if len(senha) == 0: raise ValueError
        else: self.__senha = senha
    def get_senha(self): return self.__senha

    def set_especialidade(self, especialidade):
        if len(especialidade) == 0: raise ValueError
        else: self.__especialidade = especialidade
    def get_especialidade(self): return self.__especialidade

    def to_json(self):
        return {"id": self.__id, "nome": self.__nome,  "email": self.__email, "senha": self.__senha,  "especialidade": self.__especialidade}
    @staticmethod
    def from_json(dic):
        return Profissional(dic["id"], dic["nome"], dic["email"], dic["senha"], dic["especialidade"])
    
    def __str__(self):
        return f"{self.__id} - {self.__nome} - {self.__email} - {self.__senha} - {self.__especialidade}"