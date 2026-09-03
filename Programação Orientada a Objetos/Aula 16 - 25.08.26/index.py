from templates.manterclienteui import ManterClienteUI
from templates.manterservicoui import ManterServicoUI
from templates.manterhorarioui import ManterHorarioUI
import streamlit as st

class IndexUI:
    def menu_admin():
        op = st.sidebar.selectbox("Menu", ["Cadastro de Clientes", "Cadastro de Serviços", "Cadastro de Horários"])
        if op == "Cadastro de Clientes": ManterClienteUI.main()
        if op == "Cadastro de Serviços": ManterServicoUI.main()
        if op == "Cadastro de Horários": ManterHorarioUI.main()
    def sidebar():
        IndexUI.menu_admin()
    def main():
        IndexUI.sidebar()
IndexUI.main()