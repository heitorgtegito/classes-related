from models.cliente import Cliente
import json

class ClienteDAO:
    def __init__(self):
        self.__arquivo = "clientes.json"
        self.__objetos = []
        self.__abrir()
    def inserir(self, obj):
        id = 0
        for cliente in self.__objetos:
            if cliente.get_id() > id: id = cliente.get_id()
        obj.set_id(id+1)
        self.__objetos.append(obj)
        self.__salvar
    def listar(self): return self.__objetos
    def listar_id(self, id):
        for obj in self.__objetos:
            if obj.get_id() == id: return obj
        return None
    def listar_nome(self, nome):
        for obj in self.__objetos:
            if obj.get_nome().lower.startswith(nome.lower()): return obj
        return None
    def atualizar(self, obj):
        aux = self.listar_id(obj.get_id())
        if aux != None:
            self.__objetos.remove(aux)
            self.__objetos.append(obj)
            self.__salvar()
    def excluir(self, id):
        aux = self.listar_id(id)
        if aux != None:
            self.__objetos.remove(aux)
            self.__salvar()
    def __abrir(self):
        try:
            arquivo = open(self.__arquivo, mode = "r")
            list_dic = json.load(arquivo)
            arquivo.close
            self.__objetos = []
            for dic in list_dic:
                obj = Cliente.from_json(dic)
                self.__objetos.append(obj)
        except FileNotFoundError:
            pass
    def __salvar(self):
        arquivo = open(self.__arquivo, mode = "w")
        json.dump(self.__objetos, arquivo, default=Cliente.to_json, indent=2)
        arquivo.close()