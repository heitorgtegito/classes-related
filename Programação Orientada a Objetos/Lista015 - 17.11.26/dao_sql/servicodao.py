from dao_sql.dao import DAO
from models.servico import Servico

class ServicoDAO(DAO):
    def inserir(self, obj):
        self.abrir()
        sql = '''
            INSERT INTO servico (descricao, valor)
            VALUES (?, ?)
        '''
        self.execute(sql, (obj.get_descricao(), obj.get_valor()))
        self.fechar()

    def listar(self):
        self.abrir()
        sql = 'SELECT * FROM servico'
        cursor = self.execute(sql)
        rows = cursor.fetchall()
        objs = [Servico(id, descricao, valor) for (id, descricao, valor) in rows]
        self.fechar()
        return objs

    def listar_id(self, id):
        self.abrir()
        sql = 'SELECT * FROM servico WHERE id = ?'
        cursor = self.execute(sql, (id,))
        row = cursor.fetchone()
        obj = Servico(*row) if row else None
        self.fechar()
        return obj

    def atualizar(self, obj):
        self.abrir()
        sql = '''
            UPDATE servico SET descricao=?, valor=?
            WHERE id=?
        '''
        self.execute(sql, (obj.get_descricao(), obj.get_valor(), obj.get_id()))
        self.fechar()

    def excluir(self, id):
        self.abrir()
        sql = 'DELETE FROM servico WHERE id=?'
        self.execute(sql, (id,))
        self.fechar()