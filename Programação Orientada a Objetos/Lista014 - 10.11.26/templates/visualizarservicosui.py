import streamlit as st
import pandas as pd
from service import Service
from datetime import datetime
import time

class VisualizarServicosUI:
    def main():
        st.header("Meus Serviços")
        horarios = Service.cliente_visualizar_servicos(id_cliente=st.session_state["usuario_id"])
        if len(horarios) == 0: st.write("Nenhum horário cadastrado")
        else:
            list_dic = []
            for obj in horarios: 
                profissional = Service.profissional_listar_id(obj.get_id_profissional())
                servico = Service.servico_listar_id(obj.get_id_servico())
                if profissional != None: profissional = profissional.get_nome()
                if servico != None: servico = servico.get_descricao()
                list_dic.append({"id": obj.get_id(), "data": obj.get_data(), "confirmado": obj.get_confirmado(), "serviço": servico, "profissional": profissional})
            df = pd.DataFrame(list_dic)
            st.dataframe(df)