from models.modelos import Livro


class LivroDAO:
    def cadastrar_livro(self, titulo, autor, ano_publicacao):
        livro = Livro.create(
            titulo=titulo,
            autor=autor,
            ano_publicacao=ano_publicacao,
            disponivel=True
        )
        return livro


    def get_disponiveis(self, titulo=""):
        consulta = Livro.select().where(
            Livro.disponivel == True
        )

        if titulo:
            consulta = consulta.where(
                Livro.titulo.contains(titulo)
            )

        return consulta

    def get_by_id(self, id_livro):
        return Livro.get_or_none(Livro.id == id_livro)