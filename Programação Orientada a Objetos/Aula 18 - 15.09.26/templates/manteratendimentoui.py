import streamlit as st
import pandas as pd
import time
from service import Service
from datetime import datetime

class ManterAtendimentoUI:
    def main():
        st.subheader("Cadastro de Atendimentos")
        tab1, tab2, tab3, tab4 = st.tabs(["Listar", "Inserir", "Atualizar", "Excluir"])
        with tab1: ManterAtendimentoUI.listar()
        with tab2: ManterAtendimentoUI.inserir()
        with tab3: ManterAtendimentoUI.atualizar()
        with tab4: ManterAtendimentoUI.excluir()
    def listar():
        atendimentos = Service.atendimento_listar()
        if len(atendimentos) == 0: st.write("Nenhum atendimento cadastrado")
        else:
            list_dic = []
            for obj in atendimentos:
                horario = Service.horario_listar_id(obj.get_horario_id())
                list_dic.append({"id": obj.get_id(), "data": obj.get_data(), "queixa_principal": obj.get_queixa_principal(), "historico_saude": obj.get_historico_saude(), "avaliacao": obj.get_avaliacao(), "prescricao": obj.get_prescricao(), "id_horario": horario})
            df = pd.DataFrame(list_dic)
            st.dataframe(df)
    def inserir():
        horarios = Service.horario_listar()
        data = st.selectbox("Informe o horário", horarios, index = None)
        queixa_principal = st.text_input("Informe a queixa principal")
        historico_saude = st.text_input("Informe o histórico de saúde")
        avaliacao = st.text_input("Informe a avaliação médica")
        prescricao = st.text_input("Informe a prescrição")
        if st.button("Inserir"):
            id_horario = None
            if data != None: id_horario = data.get_id()
            Service.atendimento_inserir(data, queixa_principal, historico_saude, avaliacao, prescricao, id_horario)
            st.success("Atendimento inserido com sucesso")
            time.sleep(2)
            st.rerun()
    def atualizar():
        atendimentos = Service.atendimento_listar()
        if len(atendimentos) == 0: st.write("Nenhum atendimento cadastrado")
        else:
            horarios = Service.horario_listar()
            op = st.selectbox("Atualização de atendimento", atendimentos)
            data = st.text_input("Informe a nova data e o horário do serviço", op.get_data().strftime("%d/%m/%Y %H:%M"))
            queixa_principal = st.text_input("Informe a queixa principal")
            historico_saude = st.text_input("Informe o histórico de saúde")
            avaliacao = st.text_input("Informe a avaliação médica")
            prescricao = st.text_input("Informe a prescrição")
            id_horario = None if op.get_id_horario() in [0, None] else op.get_id_horario()
            horario = st.selectbox("Informe o novo horario", horarios, next((i for i, c in enumerate(horarios) if c.get_id() == id_horario), None))
            if st.button("Atualizar"):
                id_horario = None
                if horario != None: id_horario = horario.get_id()
                Service.horario_atualizar(datetime.strptime(data, "%d/%m/%Y %H:%M"), queixa_principal, historico_saude, avaliacao, prescricao, id_horario)
                st.success("Horário atualizado com sucesso")
                time.sleep(2)
                st.rerun()
    def excluir():
        atendimentos = Service.atendimento_listar()
        if len(atendimentos) == 0: st.write("Nenhum atendimento cadastrado")
        else: 
            op = st.selectbox("Exclusão de Atendimentos", atendimentos)
            if st.button("Excluir"): 
                id = op.get_id()
                Service.atendimento_excluir(id)
                st.success("Atendimento excluído com sucesso")

