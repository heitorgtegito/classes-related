import streamlit as st
import pandas as pd
from service import Service
from datetime import datetime
import time

class ListarHorariosConfirmadosHojeUI:
    def main():
        st.header('Listar Horarios Confirmados de Hoje')
        horarios = Service.horarios_confirmados()
        if len(horarios) == 0: st.write('Nenhum horário cadastrado')
        else:
            list_dic = []
            for obj in horarios:
                cliente = Service.cliente_listar_id(obj.get_id_cliente())
                servico = Service.servico_listar_id(obj.get_id_servico())
                profissional = Service.profissional_listar_id(obj.get_id_profissional())
                if cliente != None: cliente = cliente.get_nome()
                if servico != None: servico = servico.get_descricao()
                if profissional != None: profissional = profissional.get_nome()
                list_dic.append({'id': obj.get_id(), 'data': obj.get_data(), 'cliente': cliente, 'serviço': servico, 'profissional': profissional})
            df = pd.DataFrame(list_dic)
            st.dataframe(df)