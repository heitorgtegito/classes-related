import streamlit as st
import pandas as pd
import time
from service import Service

class ManterProfissionalUI:
    def main():
        st.subheader("Cadastro de Profissionais")
        tab1, tab2, tab3, tab4 = st.tabs(["Listar", "Inserir", "Atualizar", "Excluir"])
        with tab1: ManterProfissionalUI.listar()
        with tab2: ManterProfissionalUI.inserir()
        with tab3: ManterProfissionalUI.atualizar()
        with tab4: ManterProfissionalUI.excluir()
    def listar():
        profissionais = Service.profissional_listar()
        if len(profissionais) == 0: st.write("Nenhum profissional cadastrado")
        else:
            list_dic = []
            for obj in profissionais: list_dic.append(obj.to_json())
            df = pd.DataFrame(list_dic)
            st.dataframe(df)
    def inserir():
        nome = st.text_input("Informe o nome")
        email = st.text_input("Informe o e-mail")
        especialidade = st.text_input("Informe a especialidade")
        if st.button("Inserir"):
            Service.profissional_inserir(nome, email, especialidade)
            st.success("Profissional inserido com sucesso")
            time.sleep(2)
            st.rerun()
    def atualizar():
        profissionais = Service.profissional_listar()
        if len(profissionais) == 0: st.write("Nenhum profissional cadastrado")
        else: 
            op = st.selectbox("Atualização de Profissionais", profissionais)
            nome = st.text_input("Novo nome", op.get_nome())
            email = st.text_input("Novo e-mail", op.get_email())
            especialidade = st.text_input("Nova especialidade", op.get_especialidade())
            if st.button("Atualizar"):
                id = op.get_id()
                Service.profissional_atualizar(id, nome, email, especialidade)
                st.success("Profissional atualizado com sucesso")
    def excluir():
        profissionais = Service.profissional_listar()
        if len(profissionais) == 0: st.write("Nenhum profissional cadastrado")
        else: 
            op = st.selectbox("Exclusão de Profissionais", profissionais)
            if st.button("Excluir"): 
                id = op.get_id()
                Service.profissional_excluir(id)
                st.success("Profissional excluído com sucesso")

