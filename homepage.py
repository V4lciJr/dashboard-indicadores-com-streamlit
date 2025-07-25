import streamlit as st


sessao_usuario = st.session_state

nome_usuario = None

if "username" in sessao_usuario:
    nome_usuario = sessao_usuario.name

coluna_esquerda, coluna_direita = st.columns([1, 2])

coluna_esquerda.title("Homepage")
coluna_esquerda.write(f"#### Bem vindo, {nome_usuario}")

botao_dashboards = coluna_esquerda.button("Dashboards Projetos")
botao_indicadores = coluna_esquerda.button("Principais Indicadores")


container = coluna_direita.container(border=True)
container.image("imagens/home.png")

if botao_dashboards:
    st.switch_page("dashboard.py")
elif botao_indicadores:
    st.switch_page("indicadores.py")