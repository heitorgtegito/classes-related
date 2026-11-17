from dao_sql.dao import DAO
from models.atendimentoitem import AtendimentoItem
from datetime import datetime

class AtendimentoItemDAO(DAO):
    def inserir(self, obj):
        self.abrir()
        sql = '''
            INSERT INTO atendimentoitem (qtd, valor, id_atendimento, id_servico)
            VALUES (?, ?, ?, ?, ?, ?)
        '''
        self.execute(sql, (obj.get_qtd(), obj.get_valor(), obj.get_id_atendimento(), obj.get_id_servico()))
        self.fechar()

    def listar(self):
        self.abrir()
        sql = 'SELECT * FROM atendimento'
        cursor = self.execute(sql)
        rows = cursor.fetchall()
        objs = []
        for (id, qtd, valor, id_atendimento, id_servico) in rows:
            obj = AtendimentoItem(id, qtd, valor)
            obj.set_id_atendimento(id_atendimento)
            obj.set_id_servico(id_servico)
            objs.append(obj)
        self.fechar()
        return objs

    def listar_id(self, id):
        self.abrir()
        sql = 'SELECT * FROM atendimento WHERE id = ?'
        cursor = self.execute(sql, (id,))
        row = cursor.fetchone()
        obj = None
        if row:
            obj = AtendimentoItem(row[0], row[1], row[2])
            obj.set_id_atendimento(row[3])
            obj.set_id_servico(row[4])
        self.fechar()
        return obj

    def atualizar(self, obj):
        self.abrir()
        sql = '''
            UPDATE atendimentoitem SET qtd=?, valor=?, id_atendimento=?, id_servico=?,             
            WHERE id=?
        '''
        self.execute(sql, (obj.get_qtd(), obj.get_valor(), obj.get_id_atendimento(), obj.get_id_servico(), obj.get_id()))
        self.fechar()

    def excluir(self, id):
        self.abrir()
        sql = 'DELETE FROM atendimento WHERE id=?'
        self.execute(sql, (id,))
        self.fechar()