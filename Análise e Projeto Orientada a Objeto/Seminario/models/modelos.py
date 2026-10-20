from datetime import datetime
from peewee import *

db = SqliteDatabase('biblioteca.db')

class BaseModel(Model):
    class Meta:
        database = db

class Usuario(BaseModel):
    nome = CharField()
    email = CharField(unique=True)
    senha = CharField()

    def set_nome(self, nome):
        if isinstance(nome, str) and nome.strip():
            self.nome = nome
        else:
            raise ValueError("Nome deve ser uma string não vazia.")
    def set_email(self, email):
        if isinstance(email, str) and email.strip():
            self.email = email
        else:
            raise ValueError("Email deve ser uma string não vazia.")
    def set_senha(self, senha):
        if isinstance(senha, str) and senha.strip():
            self.senha = senha
        else:
            raise ValueError("Senha deve ser uma string não vazia.")
        
class Livro(BaseModel):
    titulo = CharField()
    autor = CharField()
    ano_publicacao = IntegerField()
    disponivel = BooleanField(default=True)

    def __str__(self):
        return f"({self.id}) {self.titulo}"
    def set_titulo(self, titulo):
        if isinstance(titulo, str) and titulo.strip():
            self.titulo = titulo
        else:
            raise ValueError("Título deve ser uma string não vazia.")
    def set_disponivel(self, disponivel):
        if isinstance(disponivel, bool):
            self.disponivel = disponivel
        else:
            raise ValueError("Disponível deve ser um valor booleano.")
    def set_autor(self, autor):
        if isinstance(autor, str) and autor.strip():
            self.autor = autor
        else:
            raise ValueError("Autor deve ser uma string não vazia.")

    def set_ano_publicacao(self, ano_publicacao):
        if isinstance(ano_publicacao, int) and ano_publicacao > 0:
            self.ano_publicacao = ano_publicacao
        else:
            raise ValueError("Ano de Publicação deve ser um número inteiro positivo.")

class Emprestimo(BaseModel):
    usuario = ForeignKeyField(Usuario, backref='emprestimos')
    livro = ForeignKeyField(Livro, backref='emprestimos')
    ativo = BooleanField(default=True)
    data_emprestimo = DateTimeField(default=datetime.now)
    data_devolucao = DateTimeField(null=True)

    def set_ativo(self, ativo):
        if isinstance(ativo, bool):
            self.ativo = ativo
        else:
            raise ValueError("Ativo deve ser um valor booleano.")
    def set_data_emprestimo(self, data_emprestimo):
        if isinstance(data_emprestimo, datetime):
            self.data_emprestimo = data_emprestimo
        else:
            raise ValueError("A data do empréstimo deve ser um datetime.")

    def set_data_devolucao(self, data_devolucao):
        if data_devolucao is None or isinstance(data_devolucao, datetime):
            self.data_devolucao = data_devolucao
        else:
            raise ValueError("A data de devolução deve ser um datetime ou None.")

def criar_tabelas():
    with db:
        db.create_tables([Usuario, Livro, Emprestimo])

def carga_inicial():
    Usuario.get_or_create(
        email="matheus@email.com",
        defaults={
            "nome": "Matheus",
            "senha": "12345"
        }
    )

    Livro.get_or_create(
        titulo="Duna Parte Um",
        defaults={
            "autor": "Frank Herbert",
            "ano_publicacao": 1965
        }
    )

    Livro.get_or_create(
        titulo="Verity",
        defaults={
            "autor": "Colleen Hoover",
            "ano_publicacao": 2018
        }
    )


if __name__ == '__main__':
    criar_tabelas()
    carga_inicial()