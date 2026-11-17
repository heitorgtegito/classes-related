from dao_sql.dao import DAO
from models.atendimento import Atendimento
from datetime import datetime

class AtendimentoDAO(DAO):
    def inserir(self, obj):
        self.abrir()
        sql = '''
            INSERT INTO atendimento (data, queixa_principal, historico_saude, avaliacao, prescricao, id_horario)
            VALUES (?, ?, ?, ?, ?, ?)
        '''
        self.execute(sql, (obj.get_data().strftime('%d/%m/%Y %H:%M'), obj.get_queixa_principal(), obj.get_historico_saude(), obj.get_avaliacao(), obj.get_prescricao(), obj.get_id_horario()))
        self.fechar()

    def listar(self):
        self.abrir()
        sql = 'SELECT * FROM atendimento'
        cursor = self.execute(sql)
        rows = cursor.fetchall()
        objs = []
        for (id, data, queixa_principal, historico_saude, avaliacao, prescricao, id_horario) in rows:
            obj = Atendimento(id, datetime.strptime(data, '%d/%m/%Y %H:%M'), queixa_principal, historico_saude, avaliacao, prescricao)
            obj.set_id_horario(id_horario)
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
            obj = Atendimento(row[0], datetime.strptime(row[1], '%d/%m/%Y %H:%M'), row[2], row[3], row[4], row[5])
            obj.set_id_horario(row[6])
        self.fechar()
        return obj

    def atualizar(self, obj):
        self.abrir()
        sql = '''
            UPDATE atendimento SET data=?, queixa_principal=?, historico_saude=?,
            avaliacao=?, prescricao=?, id_horario=?
            WHERE id=?
        '''
        self.execute(sql, (obj.get_data().strftime('%d/%m/%Y %H:%M'), obj.get_queixa_principal(), obj.get_historico_saude(), obj.get_avaliacao(), obj.get_prescricao(), obj.get_id_horario(), obj.get_id()))
        self.fechar()

    def excluir(self, id):
        self.abrir()
        sql = 'DELETE FROM atendimento WHERE id=?'
        self.execute(sql, (id,))
        self.fechar()