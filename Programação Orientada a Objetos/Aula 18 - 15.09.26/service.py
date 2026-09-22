from models.cliente import Cliente         # entidade
from models.clientedao import ClienteDAO   # persistência
from models.servico import Servico
from models.servicodao import ServicoDAO
from models.horario import Horario
from models.horariodao import HorarioDAO
from models.profissional import Profissional
from models.profissionaldao import ProfissionalDAO
from models.atendimento import Atendimento
from models.atendimentodao import AtendimentoDAO


class Service:
    @staticmethod
    def cliente_inserir(nome, email, fone, senha):
        obj = Cliente(0, nome, email, fone, senha)
        ClienteDAO().inserir(obj)
    @staticmethod
    def cliente_listar():
        return ClienteDAO().listar()
    @staticmethod
    def cliente_listar_id(id):
        return ClienteDAO().listar_id(id)
    @staticmethod
    def cliente_atualizar(id, nome, email, fone, senha):
        obj = Cliente(id, nome, email, fone, senha)
        ClienteDAO().atualizar(obj)
    @staticmethod
    def cliente_excluir(id):
        ClienteDAO().excluir(id)
    
    @staticmethod
    def servico_inserir(descricao, valor):
        obj = Servico(0, descricao, valor)
        ServicoDAO().inserir(obj)
    @staticmethod
    def servico_listar():
        return ServicoDAO().listar()
    @staticmethod
    def servico_listar_id(id):
        return ServicoDAO().listar_id(id)
    @staticmethod
    def servico_atualizar(id, descricao, valor):
        obj = Servico(id, descricao, valor)
        ServicoDAO().atualizar(obj)
    @staticmethod
    def servico_excluir(id):
        ServicoDAO().excluir(id)

    @staticmethod
    def horario_inserir(data, confirmado, id_cliente, id_servico):
        obj = Horario(0, data)
        obj.set_confirmado(confirmado)
        obj.set_id_cliente(id_cliente)
        obj.set_id_servico(id_servico)
        HorarioDAO().inserir(obj)
    @staticmethod
    def horario_listar():
        return HorarioDAO().listar()
    @staticmethod
    def horario_listar_id(id):
        return HorarioDAO().listar_id(id)
    @staticmethod
    def horario_atualizar(id, data, confirmado, id_cliente, id_servico):
        obj = Horario(id, data)
        obj.set_confirmado(confirmado)
        obj.set_id_cliente(id_cliente)
        obj.set_id_servico(id_servico)
        HorarioDAO().atualizar(obj)
    @staticmethod
    def horario_excluir(id):
        HorarioDAO().excluir(id)

    @staticmethod
    def profissional_inserir(nome, email, especialidade, senha):
        obj = Profissional(0, nome, email, especialidade, senha)
        ProfissionalDAO().inserir(obj)
    @staticmethod
    def profissional_listar():
        return ProfissionalDAO().listar()
    @staticmethod
    def profissional_listar_id(id):
        return ProfissionalDAO().listar_id(id)
    @staticmethod
    def profissional_atualizar(id, nome, email, especialidade, senha):
        obj = Profissional(id, nome, email, especialidade, senha)
        ProfissionalDAO().atualizar(obj)
    @staticmethod
    def profissional_excluir(id):
        ProfissionalDAO().excluir(id)
    
    @staticmethod
    def atendimento_inserir(data, queixa_principal, historico_saude, avaliacao, prescricao, id_horario):
        obj = Atendimento(0, data, queixa_principal, historico_saude, avaliacao, prescricao)
        obj.set_id_horario(id_horario)
        AtendimentoDAO().inserir(obj)
    @staticmethod
    def atendimento_listar():
        return AtendimentoDAO().listar()
    @staticmethod
    def atendimento_listar_id(id):
        return AtendimentoDAO().listar_id(id)
    @staticmethod
    def atendimento_atualizar(id, data, queixa_principal, historico_saude, avaliacao, prescricao, id_horario):
        obj = Atendimento(id, data, queixa_principal, historico_saude, avaliacao, prescricao)
        obj.set_id_horario(id_horario)
        AtendimentoDAO().atualizar(obj)
    @staticmethod
    def atendimento_excluir(id):
        AtendimentoDAO().excluir(id)

    def cliente_criar_admin():
        for c in Service.cliente_listar():
            if c.get_email() == "admin": return
        Service.cliente_inserir("admin", "admin", "fone", "1234")

    def cliente_autenticar(email, senha):
        for c in Service.cliente_listar():
            if c.get_email() == email and c.get_senha() == senha: return {"id": c.get_id(), "nome": c.get_nome()}
        return None
    
    def profissional_autenticar(email, senha):
        for p in Service.profissional_listar():
            if p.get_email() == email and p.get_senha() == senha: return {"id": p.get_id(), "nome": p.get_nome()}
        return None