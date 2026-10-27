import streamlit as st
import pandas as pd
from service import Service
from datetime import datetime
import time

class VisualizarAgendaUI:
    def main():
        st.header("Minha Agenda")
        horarios = Service.profissional_visualizar_agenda(id_profissional=st.session_state["usuario_id"])
        if len(horarios) == 0: st.write("Nenhum horário cadastrado")
        else:
            list_dic = []
            for obj in horarios: 
                cliente = Service.cliente_listar_id(obj.get_id_cliente())
                servico = Service.servico_listar_id(obj.get_id_servico())
                if cliente != None: cliente = cliente.get_nome()
                if servico != None: servico = servico.get_descricao()
                list_dic.append({"id": obj.get_id(), "data": obj.get_data(), "confirmado": obj.get_confirmado(), "cliente": cliente, "serviço": servico})
            df = pd.DataFrame(list_dic)
            st.dataframe(df)