class Servico:
    def __init__(self, id, descricao, valor):
        self.set_id(id)
        self.set_descricao(descricao)
        self.set_valor(valor)
    def set_id(self, id):
        if id < 0: raise ValueError
        else: self.__id = id
    def get_id(self): return self.__id

    def set_descricao(self, descricao):
        if len(descricao) == 0: raise ValueError
        else: self.__descricao = descricao
    def get_descricao(self): return self.__descricao

    def set_valor(self, valor):
        if valor < 0: raise ValueError # Serviço de graça existe né
        else: self.__valor = valor
    def get_valor(self): return self.__valor

    def to_json(self):
        return {"id": self.__id, "descricao": self.__descricao,  "valor": self.__valor}
    @staticmethod
    def from_json(dic):
        return Servico(dic["id"], dic["descricao"], dic["valor"])
    
    def __str__(self):
        return f"{self.__id} - {self.__descricao} - {self.__valor}"