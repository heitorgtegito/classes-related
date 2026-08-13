import streamlit as st
from paciente import Paciente

class PacienteUI:
    def main():
        st.header("Dados do Paciente")
        nome = st.text_input("Nome: ")
        cpf = st.text_input("CPF: ")
        telefone = st.text_input("Telefone: ")
        nascimento = st.text_input("Data de Nascimento (DD/MM/AA): ")
        if st.button("Idade"):
            p = Paciente(nome, cpf, telefone, nascimento)
            st.write(p.Idade())