import sqlite3
from abc import ABC, abstractmethod

class DAO(ABC):
    def __init__(self):
        self.conn = None
        self.nome_bd = 'agenda.bd'

    def abrir(self):
        self.conn = sqlite3.connect(self.nome_bd)
        self.conn.execute('PRAGMA foreign_keys = ON')

    def fechar(self):
        self.conn.close()

    def execute(self, sql, params = None):
        cursor = self.conn.cursor()
        cursor.execute(sql, params or [])
        self.conn.commit()
        return cursor

    @abstractmethod
    def inserir(self, obj):
        pass

    @abstractmethod
    def listar(self):
        pass

    @abstractmethod
    def listar_id(self, id):
        pass

    @abstractmethod
    def atualizar(self, obj):
        pass

    @abstractmethod
    def excluir(self, id):
        pass