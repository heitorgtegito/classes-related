import streamlit as st
from service import Service
from datetime import datetime
import time

class AbrirAgendaUI:
    def main():
        st.header("Abrir Minha Agenda")
        data = st.text_input("Informe a data no formato dd/mm/aaaa", datetime.now().strftime("%d/%m/%Y"))
        horario_inicial = st.text_input("Informe o horário inicial no formato HH:MM", datetime.now().strftime("%H:%M"))
        horario_final = st.text_input("Informe o horário final no formato HH:MM", datetime.now().strftime("%H:%M"))
        intervalo = st.text_input("Informe o intervalo entre os horários (min)", datetime.now().strftime("%M"))

        if st.button("Abrir agenda"):
            Service.abrir_agenda(data, horario_inicial, horario_final, intervalo, id_usuario=st.session_state["usuario_id"])
            st.success("Agenda aberta com sucesso")
        time.sleep(2)
        st.rerun()