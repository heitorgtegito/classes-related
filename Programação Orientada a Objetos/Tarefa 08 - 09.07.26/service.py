from models.cliente import Cliente
from models.clientedao import ClienteDAO
from models.servico import Servico
from models.servicodao import ServicoDAO
from models.profissional import Profissional
from models.profissionaldao import ProfissionalDAO

class Service:
    @staticmethod
    def cliente_inserir(nome, email, telefone, senha):
        obj = Cliente(0, nome, email, telefone, senha)
        ClienteDAO().inserir(obj)
    @staticmethod
    def cliente_listar(): return ClienteDAO().listar()
    @staticmethod
    def cliente_listar_id(id): return ClienteDAO().listar_id(id)
    @staticmethod
    def cliente_listar_nome(nome): return ClienteDAO().listar_nome(nome)
    @staticmethod
    def cliente_atualizar(id, nome, email, telefone):
        obj = Cliente(id, nome, email, telefone)
        ClienteDAO().atualizar(obj)
    @staticmethod
    def cliente_excluir(id):
        ClienteDAO().excluir(id)
    @staticmethod
    def servico_inserir(id, descricao, valor):
        obj = Servico(id, descricao, valor)
        ServicoDAO().inserir(obj)
    @staticmethod
    def servico_listar(): return ServicoDAO().listar()
    @staticmethod
    def servico_listar_id(id): return ServicoDAO().listar_id(id)
    @staticmethod
    def servico_listar_descricao(descricao): return ServicoDAO().listar_descricao(descricao)
    @staticmethod
    def servico_atualizar(id, descricao, valor):
        obj = Servico(id, descricao, valor)
        ServicoDAO().atualizar(obj)
    @staticmethod
    def servico_excluir(id):
        ServicoDAO().excluir(id)
    @staticmethod
    def profissional_inserir(nome, email, senha, especialidade):
        obj = Profissional(0, nome, email, senha, especialidade)
        ProfissionalDAO().inserir(obj)
    @staticmethod
    def profissional_listar(): return ProfissionalDAO().listar()
    @staticmethod
    def profissional_pesquisar_id(id): return ProfissionalDAO().listar_id(id)
    @staticmethod
    def profissional_pesquisar_nome(nome): return ProfissionalDAO().pesquisar_nome(nome)
    @staticmethod
    def profissional_atualizar(id, descricao, valor):
        obj = Profissional(id, descricao, valor)
        ProfissionalDAO().atualizar(obj)
    @staticmethod
    def profissional_excluir(id):
        ProfissionalDAO().excluir(id)