import streamlit as st
from service import Service
from datetime import datetime, timedelta
import pandas as pd
import time

class RegistrarAtendimentoUI():
    def main():
        st.header("Registrar Atendimentos")
        horarios_disponiveis = []
        servicos = Service.servico_listar()
        for i in Service.horario_listar():
            if i.get_confirmado() == True and i.get_id_profissional() == st.session_state["usuario_id"] : horarios_disponiveis.append(i)
        if len(horarios_disponiveis) == 0: st.write("Nenhum atendimento disponível")
        else:
            data_atendimento = st.selectbox("Informe a data do atendimento", horarios_disponiveis)
            queixa_principal = st.text_input("Informe a queixa principal")
            historico_saude = st.text_area("Informe o histórico de saúde")
            avaliacao_clinica = st.text_area("Informe a avaliação clínica do paciente")
            prescricao = st.text_input("Informe a prescrição médica")

            if "id_atendimento" not in st.session_state:
                if st.button("Abrir Atendimento"):
                    atendimento = Service.atendimento_inserir(data_atendimento, queixa_principal, historico_saude, avaliacao_clinica, prescricao, data_atendimento.get_id(), 0, False)
                    st.session_state["id_atendimento"] = atendimento.get_id()
                    st.success("Atendimento aberto com sucesso")
                    time.sleep(2)
                    st.rerun()
            else:
                id_atendimento = st.session_state["id_atendimento"]
                st.subheader("Serviços Realizados")
                with st.container(border=True):
                    servico_realizado = st.selectbox("Informe o(s) serviço(s) realizado(s)", servicos)
                    quantidade = st.number_input("Informe a quantidade de serviços realizados", min_value=0, step=1)
                    if st.button("Adicionar Serviços"):
                        Service.atendimentoitem_inserir(quantidade, servico_realizado.get_valor(), id_atendimento, servico_realizado.get_id())
                        st.success("Serviço adicionado com sucesso")
                    Service.atendimentoitem_listar()
                







            if st.button("Inserir"):
                Service.atendimento_inserir(data_atendimento, queixa_principal, historico_saude, avaliacao_clinica, prescricao, servico_realizado)
                time.sleep(2)
                st.rerun()