class AtendimentoItem:
    def __init__(self, id, qtd, valor):
        self.set_id(id)
        self.set_qtd(qtd)
        self.set_valor(valor)
        self.set_id_atendimento(0)
        self.set_id_servico(0)
        
    
    def set_id(self, id):
        if id < 0: raise ValueError("Id deve ser positivo")
        self.__id = id
    def set_qtd(self, qtd):
        if qtd < 0: raise ValueError("Quantidade deve ser positiva")
        self.__qtd = qtd
    def set_valor(self, valor):
        if valor < 0: raise ValueError("Valor deve ser positivo")
        self.__valor = valor
    def set_id_atendimento(self, id_atendimento): self.__id_atendimento = id_atendimento
    def set_id_servico(self, id_servico): self.__id_servico = id_servico

    def get_id(self) : return self.__id
    def get_qtd(self) : return self.__qtd
    def get_valor(self) : return self.__valor
    def get_id_atendimento(self) : return self.__id_atendimento
    def get_id_servico(self) : return self.__id_servico

    
    def __str__(self):
        return f"{self.__id} - {self.__qtd} - {self.__valor} - {self.__id_atendimento} - {self.__id_servico}"
    
    def to_json(self):
        return { "id":self.__id, "qtd":self.__qtd, "valor":self.__valor, "id_atendimento":self.__id_atendimento, "id_servico":self.__id_servico}
    
    @staticmethod
    def from_json(dic):
        r = AtendimentoItem(dic["id"], dic["qtd"], dic["valor"])
        r.set_id_atendimento(dic["id_atendimento"])
        r.set_id_atendimento(dic["id_servico"])
        return r 