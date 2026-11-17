from dao_sql.dao import DAO
from models.cliente import Cliente

class ClienteDAO(DAO):
    def inserir(self, obj):
        self.abrir()
        sql = '''
            INSERT INTO cliente (nome, email, fone, senha)
            VALUES (?, ?, ?, ?)
        '''
        self.execute(sql, (obj.get_nome(), obj.get_email(), obj.get_fone(), obj.get_senha()))
        self.fechar()

    def listar(self):
        self.abrir()
        sql = 'SELECT * FROM cliente'
        cursor = self.execute(sql)
        rows = cursor.fetchall()
        objs = [Cliente(id, nome, email, fone, senha) for (id, nome, email, fone, senha) in rows]
        self.fechar()
        return objs

    def listar_id(self, id):
        self.abrir()
        sql = 'SELECT * FROM cliente WHERE id = ?'
        cursor = self.execute(sql, (id,))
        row = cursor.fetchone()
        obj = Cliente(*row) if row else None
        self.fechar()
        return obj

    def atualizar(self, obj):
        self.abrir()
        sql = '''
            UPDATE cliente SET nome=?, email=?, fone=?, senha=?
            WHERE id=?
        '''
        self.execute(sql, (obj.get_nome(), obj.get_email(), obj.get_fone(), obj.get_senha(), obj.get_id()))
        self.fechar()

    def excluir(self, id):
        self.abrir()
        sql = 'DELETE FROM cliente WHERE id=?'
        self.execute(sql, (id,))
        self.fechar()