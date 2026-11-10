from models.atendimentoitem import AtendimentoItem
from models.dao import DAO
import json

class AtendimentoItemDAO(DAO):
    def __init__(self):
        super().__init__("atendimentoitens.json")

    def _abrir(self):  
        try:  
            arquivo = open(self._arquivo, mode = "r")
            list_dic = json.load(arquivo)
            arquivo.close()
            self._objetos = []
            for dic in list_dic:
                obj = AtendimentoItem.from_json(dic)
                self._objetos.append(obj)
        except FileNotFoundError:
            pass

    def _salvar(self):    
        arquivo = open(self._arquivo, mode = "w")
        json.dump(self._objetos, arquivo, default = AtendimentoItem.to_json, indent = 2)
        arquivo.close()
        