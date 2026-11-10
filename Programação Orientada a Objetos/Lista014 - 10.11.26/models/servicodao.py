from models.servico import Servico
from models.dao import DAO
import json

class ServicoDAO(DAO):
    def __init__(self):
        super().__init__("servicos.json")

    def _abrir(self):  
        try:  
            arquivo = open(self._arquivo, mode = "r")
            list_dic = json.load(arquivo)
            arquivo.close()
            self._objetos = []
            for dic in list_dic:
                obj = Servico.from_json(dic)
                self._objetos.append(obj)
        except FileNotFoundError:
            pass

    def _salvar(self):    
        arquivo = open(self._arquivo, mode = "w")
        json.dump(self._objetos, arquivo, default = Servico.to_json, indent = 2)
        arquivo.close()
        