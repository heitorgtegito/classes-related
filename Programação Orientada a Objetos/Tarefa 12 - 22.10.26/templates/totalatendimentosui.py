import streamlit as st
import pandas as pd
import time
from service import Service

class TotalAtendimentosUI:
    def main():
        st.header("Total de Atendimentos")
        list_prof = Service.total_atendimentos()
        if len(list_prof) == 0: st.write("Nenhum profissional cadastrado")
        else:
            df = pd.DataFrame(list_prof)
            st.dataframe(df)