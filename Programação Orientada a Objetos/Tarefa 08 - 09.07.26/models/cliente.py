class Cliente:
    def __init__(self, id, nome, email, telefone, senha):
        self.set_id(id)
        self.set_nome(nome)
        self.set_email(email)
        self.set_telefone(telefone)
        self.set_senha(senha)
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

    def set_telefone(self, telefone):
        if len(telefone) == 0: raise ValueError
        else: self.__telefone = telefone
    def get_telefone(self): return self.__telefone

    def set_senha(self, senha):
        if len(senha) == 0: raise ValueError
        else: self.__senha = senha
    def get_senha(self): return self.__senha

    def to_json(self):
        return {"id": self.__id, "nome": self.__nome,  "email": self.__email,  "telefone": self.__telefone, "senha": self.__senha}
    @staticmethod
    def from_json(dic):
        return Cliente(dic["id"], dic["nome"], dic["email"], dic["telefone"], dic["senha"])
    
    def __str__(self):
        return f"{self.__id} - {self.__nome} - {self.__email} - {self.__telefone} - {self.__senha}"