import streamlit as st
from service import Service
import time

class AlterarSenhaUI():
    def main():
        st.header("Alterar Senha")
        senha_nova = st.text_input("Informe a nova senha", type="password")
        if st.button("Inserir"):
            Service.alterar_senha(senha_nova)
            st.success("Senha alterada com sucesso")
            time.sleep(2)
            st.rerun()