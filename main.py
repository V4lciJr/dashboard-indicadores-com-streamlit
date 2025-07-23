import streamlit as st
import pandas as pd
import streamlit_authenticator as stauth
from models import session, Usuario


lista_usuarios = session.query(Usuario).all()


credenciais = {"usernames":
    {usuario.email: {"name": usuario.nome, "password": usuario.senha} for usuario in lista_usuarios}
}

authenticator = stauth.Authenticate(credenciais, "credenciais_hasco", "ahdyagatsgedgs$rf", cookie_expiry_days=20)


def autenticar_usuario(authenticator):
    nome, status_autenticacao, username = authenticator.login()

    if status_autenticacao:
        return {"nome": nome, "username": username}

    elif status_autenticacao == False:
        st.error("Combinação de usuário e senha inválidas.")

    else:
        st.error("Preencha suas informnações, para efetuar o login.")


def logout():
    authenticator.logout()


dados_usuario = autenticar_usuario(authenticator=authenticator)


if dados_usuario:
    @st.cache_data
    def carregar_dados():
        tabela = pd.read_excel("Base.xlsx")
        return tabela


    base = carregar_dados()

    paginas = st.navigation({
        "Home": [st.Page("homepage.py", title="Início")],
        "Dashboards": [st.Page("dashboard.py", title="Dash's"), st.Page("indicadores.py", title="Indicadores")],
        "Conta": [st.Page("criar_conta.py", title="Criar conta"), st.Page(logout, title="Sair")]
    })

    paginas.run()

