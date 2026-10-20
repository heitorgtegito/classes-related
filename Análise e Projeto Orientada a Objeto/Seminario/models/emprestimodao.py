from datetime import datetime
from peewee import DoesNotExist
from models.modelos import Usuario, Livro, Emprestimo, db

class EmprestimoDAO():
    def emprestar(self, livro, usuario):
            with db.atomic(): # Vai fazer a transação ser revertida caso dê errado
                if not livro.disponivel:
                    raise ValueError("Livro indisponível para empréstimo.")
                emprestimo = Emprestimo.create(livro=livro, usuario=usuario, ativo=True, data_emprestimo=datetime.now())
                livro.disponivel = False
                livro.save()
            return emprestimo