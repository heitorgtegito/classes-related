import streamlit as st

class TelaPrincipal():

    def main(self):
        st.title("Aplicação - Meu Acervo de Livros")
        if st.button("Registrar empréstimo de livro", type="primary"):
            st.switch_page("pages/TelaEmprestimo.py")

TelaPrincipal().main()