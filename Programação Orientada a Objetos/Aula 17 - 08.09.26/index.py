from templates.manterclienteui import ManterClienteUI
from templates.manterservicoui import ManterServicoUI
from templates.manterhorarioui import ManterHorarioUI
from templates.manterprofissionalui import ManterProfissionalUI
from templates.manteratendimentoui import ManterAtendimentoUI
import streamlit as st

class IndexUI:
    def menu_admin():
        op = st.sidebar.selectbox("Menu", ["Cadastro de Clientes", "Cadastro de Serviços", "Cadastro de Horários", "Cadastro de Profissionais", "Cadastro de Atendimentos"])
        if op == "Cadastro de Clientes": ManterClienteUI.main()
        if op == "Cadastro de Serviços": ManterServicoUI.main()
        if op == "Cadastro de Horários": ManterHorarioUI.main()
        if op == "Cadastro de Profissionais": ManterProfissionalUI.main()
        if op == "Cadastro de Atendimentos": ManterAtendimentoUI.main()
    def sidebar():
        IndexUI.menu_admin()
    def main():
        IndexUI.sidebar()
IndexUI.main()