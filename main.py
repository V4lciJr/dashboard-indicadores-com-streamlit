import streamlit as st
import pandas as pd
import streamlit_authenticator as stauth


senhas_criptografadas = stauth.Hasher(["1234"]).generate()

credenciais = {"usernames": {
    "valci@hotmail.com": {"name": "Valci", "password": senhas_criptografadas[0]},
    "licia147@hotmail.com": {"name": "Licia", "password": senhas_criptografadas[0]},
    "jocyani587@hotmail.com": {"name": "Jocyani", "password": senhas_criptografadas[0]}
}}

authenticator = stauth.Authenticate(credenciais, "credenciais_hasco", "ahdyagatsgedgs$rf", cookie_expiry_days=20)


def autenticar_usuario(authenticator):
    nome, status_autenticacao, username = authenticator.login()

    if status_autenticacao:
        return {"nome": nome, "username": username}

    elif status_autenticacao == False:
        st.error("Combinação de usuário e senha inválidas.")

    else:
        st.error("Preencha suas informnações, para efetuar o login.")


def logout(authenticator):
    authenticator.logout()


dados_usuario = autenticar_usuario(authenticator=authenticator)


if dados_usuario:
    @st.cache_data
    def carregar_dados():
        tabela = pd.read_excel("Base.xlsx")
        return tabela


    base = carregar_dados()
    st.title("Dashboard e Indicadores")
    st.write("Bem vindo, Valci!!")

    st.table(base.head(10))
