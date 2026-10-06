import streamlit as st
from service import Service
import time

class RegistrarAtendimentoUI():
    def main():
        st.header("Registrar Atendimentos")
        horarios_geral = Service.horario_listar()
        horarios = []
        clientes = Service.cliente_listar()
        for i in horarios_geral:
            if i.get_id_profissional() == st.session_state["usuario_id"] and i.get_confirmado() == False: 
                horarios.append(i)
        if len(horarios) == 0: st.write("Nenhum horário disponível")
        else:
            horario = st.selectbox("Informe o horário", horarios)
            id_cliente = horario.get_id_cliente()
            cliente = st.selectbox("Cliente", Service.cliente_listar_id(id_cliente), disabled=True)
            
            if st.button("Inserir"):
                Service.registrar_atendimento(horario, cliente)
                st.success("Serviço confirmado com sucesso")
                time.sleep(2)
                st.rerun()