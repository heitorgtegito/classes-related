from templates.manterclienteui import ManterClienteUI
from templates.manterservicoui import ManterServicoUI
import streamlit as st

class IndexUI:
    def main():
        st.header("Sistema de Agendamento")
        op = st.sidebar.selectbox("Menu", ["Clientes", "Serviços"])
        if op == "Clientes": ManterClienteUI.main()
        if op == "Serviços": ManterServicoUI.main()
        
IndexUI.main()