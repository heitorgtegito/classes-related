import time
import service
import streamlit as st
from service import *

class TelaEmprestimo():
    servico = None

    def __init__(self):
        self.servico = ServicoEmprestimo()

    def inicio_emprestimo(self):
        st.header("Tela de Empréstimo de Livros")
        usuario_id = 1
        usuarios = self.servico.listar_usuario(usuario_id)
        livros = self.servico.livros_disponiveis()
        if livros:
            livro_selecionado = st.selectbox(
                "Escolha um livro para emprestar:",
                livros,
            )
        else:
            st.warning("Não há livros disponíveis para empréstimo.")
        usuario_selecionado = st.selectbox(
            "Escolha um usuario para emprestar o livro:",
            usuarios,
        )
        if livros and st.button("Registrar o Empréstimo", type="primary"):
            self.clicar_emprestar(livro_selecionado, usuario_selecionado)

    def clicar_emprestar(self, livro, usuario):
        self.servico.emprestar(livro, usuario)
        st.success("Empréstimo registrado com sucesso!")
        time.sleep(2)
        st.switch_page("index.py")

TelaEmprestimo().inicio_emprestimo()