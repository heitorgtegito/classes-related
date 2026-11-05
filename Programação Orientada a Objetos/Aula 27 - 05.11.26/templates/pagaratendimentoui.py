import streamlit as st
from service import Service
import time

class PagarAtendimentoUI():
    def main():
        st.header("Pagar Atendimento")
        atendimentos_gerais = Service.atendimento_listar()
        atendimentos = []
        clientes = Service.cliente_listar()
        for i in atendimentos_gerais:
            id_horario = i.get_id_horario()
            h = Service.horario_listar_id(id_horario)
            if i.get_pago() == False and h.get_id_cliente() == st.session_state["usuario_id"]:
                atendimentos.append(i)
        if len(atendimentos) == 0: st.write("Nenhum atendimento disponível")
        else:
            atendimento = st.selectbox("Informe o atendimento", atendimentos)
            
            if st.button("Inserir"):
                Service.pagar_atendimento(atendimento)
                st.success("Atendimento pago com sucesso")
                time.sleep(2)
                st.rerun()