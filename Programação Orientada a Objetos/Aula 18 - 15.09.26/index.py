from templates.manterclienteui import ManterClienteUI
from templates.manterservicoui import ManterServicoUI
from templates.manterhorarioui import ManterHorarioUI
from templates.manterprofissionalui import ManterProfissionalUI
from templates.manteratendimentoui import ManterAtendimentoUI
from templates.abrircontaui import AbrirContaUI
from templates.loginui import LoginUI
from templates.perfilclienteui import PerfilClienteUI
from templates.perfilprofissionalui import PerfilProfissionalUI
from service import Service
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
        if "usuario_id" not in st.session_state:
            IndexUI.menu_visitante()
        else:
            admin = st.session_state["usuario_nome"] == "admin"
            st.sidebar.write("Bem-vindo(a), " + st.session_state["usuario_nome"])
            if admin: IndexUI.menu_admin()
            else: 
                if st.session_state["usuario_tipo"] == "cliente": IndexUI.menu_cliente()
                elif st.session_state["usuario_tipo"] == "profissional": IndexUI.menu_profissional()
            IndexUI.sair_do_sistema()
    def main():
        Service.cliente_criar_admin()
        IndexUI.sidebar()
    def menu_visitante():
        op = st.sidebar.selectbox("Menu", ["Entrar no Sistema","Abrir Conta"])
        if op == "Entrar no Sistema": LoginUI.main()
        if op == "Abrir Conta": AbrirContaUI.main()
    def menu_cliente():
        op = st.sidebar.selectbox("Menu", ["Meus Dados"])
        if op == "Meus Dados": PerfilClienteUI.cliente_main()
    def menu_profissional():
        op = st.sidebar.selectbox("Menu", ["Meus Dados"])
        if op == "Meus Dados": PerfilProfissionalUI.profissional_main()
    def sair_do_sistema():
        if st.sidebar.button("Sair"):
            del st.session_state["usuario_id"]
            del st.session_state["usuario_nome"]
            st.rerun()

IndexUI.main()