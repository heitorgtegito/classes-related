import time
import service
import streamlit as st
from service import *

class TelaLivros():
    servico = None

    def __init__(self):
        self.servico = ServicoLivro()

    def cadastrar_livro(self):
        st.header("Cadastro de Livros")
        titulo = st.text_input("Título do Livro")
        autor = st.text_input("Autor do Livro")
        ano_publicacao = st.number_input("Ano de Publicação", min_value=1, step=1)

        if st.button("Cadastrar Livro", type="primary"):
            self.clicar_cadastrar(titulo, autor, ano_publicacao)

    def clicar_cadastrar(self, titulo, autor, ano_publicacao):
        self.servico.cadastrar_livro(titulo, autor, ano_publicacao)
        st.success("Livro cadastrado com sucesso!")
        time.sleep(2)
        st.switch_page("index.py")

TelaLivros().cadastrar_livro()