import streamlit as st
from models.modelos import criar_tabelas

criar_tabelas()

pages = {
    "Pessoal": [
        st.Page(
            "pages/TelaPrincipal.py",
            title="Página Principal"
        ),
        st.Page(
            "pages/TelaEmprestimo.py",
            title="Tela de Empréstimo"
        ),
        st.Page(
            "pages/telalivros.py",
            title="Tela de Livros"
        ),
        st.Page(
            "pages/telausuario.py",
            title="Tela de Usuários"
        ),
    ],
}

pg = st.navigation(pages)
pg.run()
