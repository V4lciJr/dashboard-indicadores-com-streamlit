import streamlit as st
import streamlit_authenticator as stauth
from models import session, Usuario
from time import sleep

st.title("Criar Conta")


form = st.form("form_criar_conta")

nome_usuario = form.text_input("Nome")
email_usuario = form.text_input("E-mail")
senha_usuario = form.text_input("Senha", type="password")
admin = form.checkbox("É um admin?")
botao_submit = form.form_submit_button("Enviar")

if botao_submit:
    lista_usuarios_existentes = session.query(Usuario).filter_by(email=email_usuario).all()

    if lista_usuarios_existentes:
        st.write("Já existe um usuário, com esse e-mail cadastrado.")
    elif not email_usuario:
        st.write("Você precisa digitar seu e-mail para cadastro")
    else:
        senha_criptografada = stauth.Hasher([senha_usuario]).generate()[0]
        usario = Usuario(nome=nome_usuario, senha=senha_criptografada, email=email_usuario, admin=admin)
        session.add(usario)
        session.commit()
        st.write("Usuário cadastrado com sucesso!!")
        sleep(1)
        st.switch_page("homepage.py")
