import plotly.express as px
from importar_dados import *
from ia_agents import agente

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

oportunidades = base['Código Projeto'].count()
projetos_fechados = base_fechados['Código Projeto'].count()
em_andamento = base_andamento['Código Projeto'].count()

criar_card("oportunidades.png", f"{oportunidades}", "Oportunidades", coluna_esquerda)
criar_card("projetos_fechados.png", f"{projetos_fechados}", "Projetos Fechados", coluna_meio)
criar_card("em_andamento.png", f"{em_andamento}", "Em Andamento", coluna_direita)

total_orcado = base_fechados['Valor Orçado'].sum()
total_pago = base_fechados['Valor Negociado'].sum()
desconto = base_fechados['Desconto Concedido'].sum()

criar_card("total_orcado.png", f"R$ {total_orcado:,.2f}", "Total Orçado", coluna_esquerda)
criar_card("total_pago.png", f"R$ {total_pago:,.2f}", "Total Pago", coluna_meio)
criar_card("desconto.png", f"R$ {desconto:,.2f}", "Total Desconto", coluna_direita)

base_status = base.groupby("Status", as_index=False).count()
base_status = base_status.rename(columns={'Código Projeto': 'Quantidade'})
base_status = base_status.sort_values(by='Quantidade', ascending=False)

grafico_funil = px.funnel(base_status, x="Quantidade", y="Status")
st.plotly_chart(grafico_funil)

resumo = agente(
    f"""A página apresenta os indicadores dessa base{base}, ela foca na principalmente na aba de status, então temos as
    oportunidades de projetos {oportunidades}, a quantidade de projetos fechados {projetos_fechados} e em andamento {em_andamento},
    bem como temos os valores, as receitas dessa base ao longo dos anos, ao das datas.
    Os valores são:
        total_orcado {total_orcado}
        total pago {total_pago}
        valor de desconto {desconto}
        
        Não traga números, apenas as análises e porcetagens, seja de crescimento ou de queda.
        devolva um resumo e uma análise sobre esses dados, pode utilizar emojis para explicar e ilustar melhor a análise,
        devola apenas os dados e mais nenhum texto adicional

        """
)

st.write("### Resumo:")
st.write(resumo)
