import plotly.express as px
from importar_dados import *

base = carregar_dados()


def criar_card(icone, dado, texto, coluna_card):
    container = coluna_card.container(border=True)
    coluna_esquerda, coluna_direita = container.columns([1, 2.5])
    coluna_esquerda.image(f"imagens/{icone}")
    coluna_direita.write(dado)
    coluna_direita.write(texto)


coluna_esquerda, coluna_meio, coluna_direita = st.columns([1, 1, 1])

base_andamento = base[base["Status"] == "Em andamento"]
base_fechados = base[base["Status"].isin(["Em andamento", "Finalizado"])]

criar_card("oportunidades.png", f"{base['Código Projeto'].count()}", "Oportunidades", coluna_esquerda)
criar_card("projetos_fechados.png", f"{base_fechados['Código Projeto'].count()}", "Projetos Fechados", coluna_meio)
criar_card("em_andamento.png", f"{base_andamento['Código Projeto'].count()}", "Em Andamento", coluna_direita)

criar_card("total_orcado.png", f"R$ {base_fechados['Valor Orçado'].sum():,.2f}", "Total Orçado", coluna_esquerda)
criar_card("total_pago.png", f"R$ {base_fechados['Valor Negociado'].sum():,.2f}", "Total Pago", coluna_meio)
criar_card("desconto.png", f"R$ {base_fechados['Desconto Concedido'].sum():,.2f}", "Total Desconto", coluna_direita)

base_status = base.groupby("Status", as_index=False).count()
base_status = base_status.rename(columns={'Código Projeto': 'Quantidade'})
base_status = base_status.sort_values(by='Quantidade', ascending=False)

grafico_funil = px.funnel(base_status, x="Quantidade", y="Status")
st.plotly_chart(grafico_funil)

