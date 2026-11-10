import streamlit as st
import pandas as pd
import time
from service import Service

class TotalAtendimentosUI:
    def main():
        st.header('Total de Atendimentos')
        dt_inicial = st.date_input('Data inicial')
        dt_final = st.date_input('Data final')
        list_prof = Service.total_atendimentos(dt_inicial, dt_final)
        if dt_inicial <= dt_final:
            list_prof = Service.total_atendimentos(dt_inicial, dt_final)
            if len(list_prof) == 0: st.write('Nenhum profissional cadastrado')
            else:
                profissionais = Service.profissional_listar()
                dados = []

                for p in profissionais:
                    dados.append({'Profissional': p.get_nome(), 'Total de atendimentos': list_prof.get(p.get_id(), 0)})

                df = pd.DataFrame(dados)
                st.dataframe(df, hide_index=True)
        else:
            st.error('A data inicial deve ser anterior ou igual à data final.')