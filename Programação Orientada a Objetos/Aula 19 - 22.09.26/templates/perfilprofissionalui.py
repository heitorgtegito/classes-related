import streamlit as st
from service import Service
import time

class PerfilProfissionalUI:
    def profissional_main():
        st.header("Meus Dados")
        op = Service.profissional_listar_id(st.session_state["usuario_id"])
        nome = st.text_input("Informe o novo nome", op.get_nome())
        email = st.text_input("Informe o novo e-mail", op.get_email())
        especialidade = st.text_input("Informe a nova especialidade", op.get_especialidade())
        senha = st.text_input("Informe a nova senha", op.get_senha(), type="password")
        if st.button("Atualizar"): 
            id = op.get_id()
            Service.profissional_atualizar(id, nome, email, especialidade, senha)
            st.success("Profissional atualizado com sucesso")