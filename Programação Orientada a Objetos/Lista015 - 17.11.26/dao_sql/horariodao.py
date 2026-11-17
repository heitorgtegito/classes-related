from dao_sql.dao import DAO
from models.horario import Horario
from datetime import datetime

class HorarioDAO(DAO):
    def inserir(self, obj):
        self.abrir()
        sql = '''
            INSERT INTO horario (data, confirmado, id_cliente, id_servico, id_profissional)
            VALUES (?, ?, ?, ?, ?)
        '''
        self.execute(sql, (obj.get_data().strftime('%d/%m/%Y %H:%M'), obj.get_confirmado(), obj.get_id_cliente(), obj.get_id_servico(), obj.get_id_profissional()))
        self.fechar()

    def listar(self):
        self.abrir()
        sql = 'SELECT * FROM horario'
        cursor = self.execute(sql)
        rows = cursor.fetchall()
        objs = []
        for (id, data, confirmado, id_cliente, id_servico, id_profissional) in rows:
            obj = Horario(id, datetime.strptime(data, '%d/%m/%Y %H:%M'))
            obj.set_confirmado(bool(confirmado))
            obj.set_id_cliente(id_cliente)
            obj.set_id_servico(id_servico)
            obj.set_id_profissional(id_profissional)
            objs.append(obj)
        self.fechar()
        return objs

    def listar_id(self, id):
        self.abrir()
        sql = 'SELECT * FROM horario WHERE id = ?'
        cursor = self.execute(sql, (id,))
        row = cursor.fetchone()
        obj = None
        if row:
            obj = Horario(row[0], datetime.strptime(row[1], '%d/%m/%Y %H:%M'))
            obj.set_confirmado(bool(row[2]))
            obj.set_id_cliente(row[3])
            obj.set_id_servico(row[4])
            obj.set_id_profissional(row[5])
        self.fechar()
        return obj

    def atualizar(self, obj):
        self.abrir()
        sql = '''
            UPDATE horario SET data=?, confirmado=?, id_cliente=?, id_servico=?, id_profissional=?
            WHERE id=?
        '''
        self.execute(sql, (obj.get_data().strftime('%d/%m/%Y %H:%M'), obj.get_confirmado(), obj.get_id_cliente(), obj.get_id_servico(), obj.get_id_profissional(), obj.get_id()))
        self.fechar()

    def excluir(self, id):
        self.abrir()
        sql = 'DELETE FROM horario WHERE id=?'
        self.execute(sql, (id,))
        self.fechar()