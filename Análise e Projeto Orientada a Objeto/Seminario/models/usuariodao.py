from models.modelos import Usuario
class UsuarioDAO():
    def cadastrar_usuario(self, nome, email, senha):
        usuario = Usuario.create(
            nome=nome,
            email=email,
            senha=senha
        )
        return usuario
    def get_usuarios(self):
        return Usuario.select()
    def get_by_id(self, id_usuario):
        return Usuario.get_or_none(Usuario.id == id_usuario) 