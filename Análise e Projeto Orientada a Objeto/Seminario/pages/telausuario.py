import time
import service
import streamlit as st
from service import *

class TelaUsuario():
    servico = None

    def __init__(self):
        self.servico = ServicoUsuario()

    def cadastrar_usuario(self):
        st.header("Cadastro de Usuários")
        nome = st.text_input("Nome do Usuário")
        email = st.text_input("Email do Usuário")
        senha = st.text_input("Senha do Usuário", type="password")

        if st.button("Cadastrar Usuário", type="primary"):
            self.clicar_cadastrar(nome, email, senha)

    def clicar_cadastrar(self, nome, email, senha):
        self.servico.cadastrar_usuario(nome, email, senha)
        st.success("Usuário cadastrado com sucesso!")
        time.sleep(2)
        st.switch_page("index.py")

TelaUsuario().cadastrar_usuario()