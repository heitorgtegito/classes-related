import streamlit as st
import pandas as pd
import time
from service import Service

class ManterServicoUI:
    def main():
        st.subheader("Cadastro de Serviços")
        tab1, tab2, tab3, tab4 = st.tabs(["Listar", "Inserir", "Atualizar", "Excluir"])
        with tab1: ManterServicoUI.listar()
        with tab2: ManterServicoUI.inserir()
        with tab3: ManterServicoUI.atualizar()
        with tab4: ManterServicoUI.excluir()
    def listar():
        servicos = Service.servico_listar()
        if len(servicos) == 0: st.write("Nenhum serviço cadastrado")
        else:
            list_dic = []
            for obj in servicos: list_dic.append(obj.to_json())
            df = pd.DataFrame(list_dic)
            st.dataframe(df)
    def inserir():
        descricao = st.text_input("Informe a descrição")
        valor = st.text_input("Informe o valor")
        if st.button("Inserir"):
            try:
                Service.servico_inserir(descricao, float(valor))
                st.success("Serviço inserido com sucesso")
            except ValueError as erro:
                st.error(erro)
            time.sleep(2)
            st.rerun()
    def atualizar():
        servicos = Service.servico_listar()
        if len(servicos) == 0: st.write("Nenhum serviço cadastrado")
        else: 
            op = st.selectbox("Atualização de Serviços", servicos)
            descricao = st.text_input("Nova descrição", op.get_descricao())
            valor = st.text_input("Novo valor", op.get_valor())
            if st.button("Atualizar"):
                try:
                    id = op.get_id()
                    Service.servico_atualizar(id, descricao, float(valor))
                    st.success("Serviço atualizado com sucesso")
                except ValueError as erro:
                    st.error(erro)
                time.sleep(2)
                st.rerun()
    def excluir():
        servicos = Service.servico_listar()
        if len(servicos) == 0: st.write("Nenhum serviço cadastrado")
        else:
            op = st.selectbox("Exclusão de Serviços", servicos)
            try:
                if st.button("Excluir"): 
                    id = op.get_id()
                    Service.servico_excluir(id)
                    st.success("Serviço excluído com sucesso")
            except ValueError as erro:
                st.error(erro)
            time.sleep(2)
            st.rerun()

