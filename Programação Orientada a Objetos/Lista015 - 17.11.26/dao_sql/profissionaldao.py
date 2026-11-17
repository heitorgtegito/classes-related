from dao_sql.dao import DAO
from models.profissional import Profissional

class ProfissionalDAO(DAO):
    def inserir(self, obj):
        self.abrir()
        sql = '''
            INSERT INTO profissional (nome, email, especialidade, senha)
            VALUES (?, ?, ?, ?)
        '''
        self.execute(sql, (obj.get_nome(), obj.get_email(), obj.get_especialidade(), obj.get_senha()))
        self.fechar()

    def listar(self):
        self.abrir()
        sql = 'SELECT * FROM profissional'
        cursor = self.execute(sql)
        rows = cursor.fetchall()
        objs = [Profissional(id, nome, email, especialidade, senha) for (id, nome, email, especialidade, senha) in rows]
        self.fechar()
        return objs

    def listar_id(self, id):
        self.abrir()
        sql = 'SELECT * FROM profissional WHERE id = ?'
        cursor = self.execute(sql, (id,))
        row = cursor.fetchone()
        obj = Profissional(*row) if row else None
        self.fechar()
        return obj

    def atualizar(self, obj):
        self.abrir()
        sql = '''
            UPDATE profissional SET nome=?, email=?, especialidade=?, senha=?
            WHERE id=?
        '''
        self.execute(sql, (obj.get_nome(), obj.get_email(), obj.get_especialidade(), obj.get_senha(), obj.get_id()))
        self.fechar()

    def excluir(self, id):
        self.abrir()
        sql = 'DELETE FROM profissional WHERE id=?'
        self.execute(sql, (id,))
        self.fechar()