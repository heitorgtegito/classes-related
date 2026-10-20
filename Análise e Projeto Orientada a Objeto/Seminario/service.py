from models.usuariodao import *
from models.emprestimodao import *
from models.livrodao import *


class ServicoEmprestimo():
    dao_usuario = None
    dao_livros = None
    dao_emprestimos = None

    def __init__(self):
        self.dao_usuario = UsuarioDAO()
        self.dao_livros = LivroDAO()
        self.dao_emprestimos = EmprestimoDAO()

    def listar_usuario(self, usr_id):
        user = self.dao_usuario.get_by_id(usr_id)
        return user.nome

    def livros_disponiveis(self, titulo=""):
        return self.dao_livros.get_disponiveis(titulo)

    def emprestar(self, livro, usuario):
        if livro is None: raise ValueError("Livro não encontrado.")
        if usuario is None: raise ValueError("Usuário não encontrado.")
        if livro.disponivel == False: raise ValueError("Livro indisponível para empréstimo.")

        return self.dao_emprestimos.emprestar(livro, usuario)

class ServicoLivro():
    dao_livros = None

    def __init__(self):
        self.dao_livros = LivroDAO()

    def cadastrar_livro(self, titulo, autor, ano_publicacao):
        if not titulo or not autor or not ano_publicacao:
            raise ValueError("Todos os campos são obrigatórios.")
        if not isinstance(ano_publicacao, int) or ano_publicacao <= 0:
            raise ValueError("Ano de publicação deve ser um número inteiro positivo.")

        return self.dao_livros.cadastrar_livro(titulo, autor, ano_publicacao)

class ServicoUsuario():
    dao_usuario = None

    def __init__(self):
        self.dao_usuario = UsuarioDAO()

    def cadastrar_usuario(self, nome, email, senha):
        if not nome or not email or not senha:
            raise ValueError("Todos os campos são obrigatórios.")
        if not isinstance(nome, str) or not isinstance(email, str) or not isinstance(senha, str):
            raise ValueError("Nome, email e senha devem ser strings.")

        return self.dao_usuario.cadastrar_usuario(nome, email, senha)