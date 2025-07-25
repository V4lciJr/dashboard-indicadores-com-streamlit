import plotly.express as px
import plotly.graph_objects as go
from importar_dados import *
from ia_agents import agente

base = carregar_dados()


coluna_esquerda, coluna_meio, _ = st.columns([1, 1, 1])

setor = coluna_esquerda.selectbox("Setor", list(base['Setor'].unique()))
status = coluna_meio.selectbox("Status", list(base['Status'].unique()))

base_filtrada = base[(base['Setor'] == setor) & (base['Status'] == status)]
base_mensal = base_filtrada.groupby(base_filtrada['Data Chegada'].dt.to_period('M')).sum(numeric_only=True).reset_index()
base_mensal['Data Chegada'] = base_mensal['Data Chegada'].dt.to_timestamp()

container = st.container(border=True)
with container:

    st.write("### Total de Projetos por mês (R$)")

    # grafico de area
    grafico_area = px.area(base_mensal, x="Data Chegada", y="Valor Negociado")
    st.plotly_chart(grafico_area)

    # Filtros
    coluna_esquerda, coluna_direita = st.columns([3, 1])
    coluna_esquerda.write("### Comparação Orçado x Pago")

    base_mensal['Ano'] = base_mensal['Data Chegada'].dt.year
    lista_anos = list(base_mensal['Ano'].unique())

    ano_selecionado = coluna_direita.selectbox("Ano", lista_anos)

    base_mensal = base_mensal[base_mensal['Ano'] == ano_selecionado]
    total_pago = base_mensal['Valor Negociado'].sum()
    total_desconto = base_mensal['Desconto Concedido'].sum()

    # metricas
    coluna_esquerda, coluna_direita = st.columns([1, 1])
    coluna_esquerda.metric("Total Pago", f'R$ {total_pago:,.2f}')
    coluna_direita.metric("Total Desconto", f'R$ {total_desconto:,.2f}')

    # grafico de colunas
    grafico_barra = go.Figure(data=[
        go.Bar(name="Valor Orçado", x=base_mensal["Data Chegada"], y=base_mensal["Valor Orçado"], text=base_mensal["Valor Orçado"]),
        go.Bar(name="Valor Pago", x=base_mensal["Data Chegada"], y=base_mensal["Valor Negociado"], text=base_mensal["Valor Negociado"])
    ])

    grafico_barra.update_layout(barmode='group')
    st.plotly_chart(grafico_barra)

    resumo = agente(
        f"""Você receberá uma base de projetos, com valores orçados, valores negociados e desconto concedidos, a base
        também possui os tipos de projetos e seus status de acordo com as datas.
        Faça um resumo e uma análise dos dados apresentados nessa base {base_mensal}, seja sempre preciso e objetivo,
        sempre traga insights relacionados ao dados que auxílie na tomada de decisão e ajude a melhorarmos os números,
        traga apenas as informações e mais nada, não traga números, apenas análises.
        utilize emojis para explicar e ilustar melhor a análise
        
        """
    )

st.write("### Resumo:")
st.write(resumo)
