class PlayList:
    def __init__(self, id, nome, descricao):
        self.set_id(id)
        self.set_nome(nome)
        self.set_descricao(descricao)

    def set_id(self, id):
        if id <= 0: raise ValueError()
        else: self.__id = id
    def get_id(self): return self.__id

    def set_nome(self, nome):
        if len(nome) == 0: raise ValueError()
        else: self.__nome = nome
    def get_nome(self): return self.__nome

    def set_descricao(self, descricao): 
        self.__descricao = descricao # acredito que a playlist possa ou não ter descrição
    def get_descricao(self): return self.__descricao

    def __str__(self):
        return f"{self.__id} - {self.__nome} - {self.__descricao}"


class Musica:
    def __init__(self, id, titulo, artista, album):
        self.set_id(id)
        self.set_titulo(titulo)
        self.set_artista(artista)
        self.set_album(album)

    def set_id(self, id):
        if id <= 0: raise ValueError()
        else: self.__id = id
    def get_id(self): return self.__id

    def set_titulo(self, titulo):
        if len(titulo) == 0: raise ValueError()
        else: self.__titulo = titulo
    def get_titulo(self): return self.__titulo
         
    def set_artista(self, artista):
        if len(artista) == 0: raise ValueError()
        else: self.__artista = artista
    def get_artista(self): return self.__artista

    def set_album(self, album):
        self.__album = album # acho que dá pra postar música sem ser em álbum
    def get_album(self): return self.__album

    def __str__(self):
        return f"{self.__id} - {self.__titulo} - {self.__artista} - {self.__album}"


class PlayListItem:
    def __init__(self, id, id_playlist, id_musica, sequencia):
        self.set_id(id)
        self.set_id_playlist(id_playlist)
        self.set_id_musica(id_musica)
        self.set_sequencia(sequencia)

    def set_id(self, id):
        if id <= 0: raise ValueError()
        else: self.__id = id
    def get_id(self): return self.__id

    def set_id_playlist(self, id_playlist):
        self.__id_playlist = id_playlist
    def get_id_playlist(self): return self.__id_playlist

    def set_id_musica(self, id_musica):
        self.__id_musica = id_musica
    def get_id_musica(self): return self.__id_musica

    def set_sequencia(self, sequencia):
        self.__sequencia = sequencia
    def get_sequencia(self): return self.__sequencia

    def __str__(self):
        return f"{self.__id} - Playlist {self.__id_playlist} - Música {self.__id_musica} - Faixa {self.__sequencia}"


class UI:
    playlists = []
    musicas = []
    itens = []

    @staticmethod
    def main():
        op = 0
        while op != 10:
            op = UI.menu()
            if op == 1: UI.inserir_playlist()
            if op == 2: UI.listar_playlists()
            if op == 3: UI.inserir_musica()
            if op == 4: UI.listar_musicas()
            if op == 5: UI.inserir_item()
            if op == 6: UI.listar_itens()
            if op == 7: UI.atualizar_playlist()
            if op == 8: UI.atualizar_musica()
            if op == 9: UI.atualizar_item()

    @staticmethod
    def menu():
        print("1-Inserir Playlist \n2-Listar Playlists \n3-Inserir Música \n4-Listar Músicas \n5-Inserir Item \n6-Listar Itens \n7-Atualizar Playlist \n8-Atualizar Música \n9-Atualizar Item \n10-Sair")
        return int(input("Escolha uma opção: "))

    @classmethod
    def inserir_playlist(cls):
        id = int(input("Id da playlist: "))
        nome = input("Nome: ")
        descricao = input("Descrição: ")
        x = PlayList(id, nome, descricao)
        cls.playlists.append(x)

    @classmethod
    def listar_playlists(cls):
        for x in cls.playlists:
            print(x)

    @classmethod
    def inserir_musica(cls):
        id = int(input("Id da música: "))
        titulo = input("Título: ")
        artista = input("Artista: ")
        album = input("Álbum: ")
        x = Musica(id, titulo, artista, album)
        cls.musicas.append(x)

    @classmethod
    def listar_musicas(cls):
        for x in cls.musicas:
            print(x)

    @classmethod
    def inserir_item(cls):
        id = int(input("Id do item: "))
        id_playlist = int(input("Id da playlist: "))
        id_musica = int(input("Id da música: "))
        sequencia = int(input("Sequência: "))
        x = PlayListItem(id, id_playlist, id_musica, sequencia)
        cls.itens.append(x)

    @classmethod
    def listar_itens(cls):
        for x in cls.itens:
            print(x)

    @classmethod
    def procurar_playlist(cls, id):
        for x in cls.playlists:
            if x.get_id() == id:
                return x
        return None

    @classmethod
    def atualizar_playlist(cls):
        cls.listar_playlists()
        id = int(input("Informe o id da playlist: "))
        x = cls.procurar_playlist(id)
        if x != None:
            cls.playlists.remove(x)
            nome = input("Novo nome: ")
            descricao = input("Nova descrição: ")
            nova = PlayList(id, nome, descricao)
            cls.playlists.append(nova)

    @classmethod
    def procurar_musica(cls, id):
        for x in cls.musicas:
            if x.get_id() == id:
                return x
        return None

    @classmethod
    def atualizar_musica(cls):
        cls.listar_musicas()
        id = int(input("Informe o id da música: "))
        x = cls.procurar_musica(id)
        if x != None:
            cls.musicas.remove(x)
            titulo = input("Novo título: ")
            artista = input("Novo artista: ")
            album = input("Novo álbum: ")
            nova = Musica(id, titulo, artista, album)
            cls.musicas.append(nova)

    @classmethod
    def procurar_item(cls, id):
        for x in cls.itens:
            if x.get_id() == id:
                return x
        return None

    @classmethod
    def atualizar_item(cls):
        cls.listar_itens()
        id = int(input("Informe o id do item: "))
        x = cls.procurar_item(id)
        if x != None:
            cls.itens.remove(x)
            id_playlist = int(input("Novo id da playlist: "))
            id_musica = int(input("Novo id da música: "))
            sequencia = int(input("Nova sequência: "))
            novo = PlayListItem(id, id_playlist, id_musica, sequencia)
            cls.itens.append(novo)

UI.main()