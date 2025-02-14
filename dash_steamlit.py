import streamlit as st
import pandas as pd
import plotly.express as px
import altair as alt
st.set_page_config(page_title="Dashboard de Dados Meteorológicos", layout="wide")
import streamlit as st

# Adicionar CSS para personalizar o layout, o fundo e a imagem
st.markdown(
    """
    <style>
    /* Alterar fundo de toda a página */
    .stApp {
        background-color:rgb(255, 255, 255); /
    }

    /* Centralizar o conteúdo e controlar largura */
    .main {
        max-width: 85%; /* Define a largura máxima */
        margin: 0 auto; /* Centraliza horizontalmente */
        padding: 20px; /* Adiciona espaço interno */
        border-radius: 10px; /* Suaviza bordas */
    }

    /* Centralizar a imagem e configurar tamanho */
    .logo-container {
        text-align: center; /* Centralizar a imagem */
        margin-bottom: 20px; /* Espaço abaixo da imagem */
    }

    .logo-container img {
        width: 50%; /* Largura da imagem */
        height: auto; /* Manter proporção */
        border-radius: 10px; /* Suavizar bordas da imagem */
    }
        
    """,
    unsafe_allow_html=True
)

# Tente carregar a imagem usando o caminho correto


# Exemplo de uso de uma outra imagem com o st.image
#st.image("logo l.png", width=200)

#parte de pegar os dados
topo = ['Date', 'Time','Temperatura (°C)', 'Hi temp (°C)', 'Low Temp (°C)', 'Umidade (%)', 'Dew Pt. (°C)', 'Velocidade do Vento (m/s)', 'Wind Dir', 'Wind Run (m/s)', 'Hi Speed (m/s)', 'Hi Dir', 'Wind Chill', 'Heat Index', 'THW Index', 'THSW Index', 'Pressão Atm.', 'Precipitação', 'Rain Rate (mm)', 'Solar Rad', 'Solar Energy', 'Hi Solar Rad', 'UVI', 'UV Dose', 'Hi UV', 'Heat D-D', 'Cool D-D', 'In Temp', 'In Hum', 'In Dew', 'In Heat', 'In EMC', 'In Air Density', 'ET', 'Wind Samp', 'Wind TX', 'ISS Recept', 'Arc Int.']
dados = '1213.txt'
topo2 = ['Temperatura (°C)', 'Hi temp (°C)', 'Low Temp (°C)', 'Umidade (%)', 'Dew Pt. (°C)', 'Velocidade do Vento (m/s)', 'Wind Dir ', 'Wind Run (m/s)', 'Hi Speed (m/s)', 'Hi Dir', 'Wind Chill', 'Heat Index', 'THW Index', 'THSW Index', 'Pressão Atm.', 'Precipitação', 'Rain Rate (mm)', 'Solar Rad', 'Solar Energy', 'Hi Solar Rad', 'UVI', 'UV Dose', 'Hi UV', 'Heat D-D', 'Cool D-D', 'In Temp', 'In Hum', 'In Dew', 'In Heat', 'In EMC', 'In Air Density', 'ET', 'Wind Samp', 'Wind TX', 'ISS Recept', 'Arc Int.']

davis = pd.read_csv(dados, sep='\t', dtype={'Temp OUT': float, 'Out Hum': float, 'Rain': float, 'UV Index': float, 'UV Dose': float, 'Bar': float, 'Dew Pt.': float, 'Heat Index': float}, na_values=['---', '------'], header=1, names=topo)
davis['Dat']=davis['Date']
davis["Date"] = pd.to_datetime(davis["Date"])
davis['Dia'] = davis['Date'].dt.day
davis['Year'] = davis['Date'].dt.year
davis['Mês'] = davis['Date'].dt.month

# Definindo as variáveis para as opções no Streamlit
anos_lista = list(davis['Year'].unique())
meses_lista = list(davis['Mês'].unique())
anos_lista_analise_1=anos_lista
dias_lista=list(davis['Dat'].unique())
variaveis=list(topo2)
variaveis_analise1=variaveis
tipos_de_analise=list(['Média','Máximos','Minimos'])
selecao_1=list(['Gráfico','Tabela'])
# Usando HTML para estilizar o título
st.markdown('<h1 style="color:orange">Dashboard de Dados Meteorológicos - Vantage Pro 2</h1>', unsafe_allow_html=True)


# Seleção de ano , mês e dia
#mes_selecionado = st.selectbox('Selecione o mês', meses_lista, index=0)



# Filtrando os dados
#davis_selecionado = davis[(davis['Year'] == ano_selecionado) & (davis['Mês'] == mes_selecionado)]
anual_mensal=st.radio('Escolha entre análises anuais, diárias e mensais',['Diária','Anual','Mensal'])

if anual_mensal == 'Diária':
    dia_selecionado = st.selectbox('Selecione o dia',dias_lista,index=2)
    variavel_grafico=st.selectbox('Selecione a variável para graficar',variaveis,index=2)
    davis_selecionado1 = davis[davis['Date'] == dia_selecionado]
    davis_selecionado1.loc[:, 'Hora'] = davis_selecionado1['Time']
    davis_selecionado1.loc[:, 'Hi Dir'] = davis_selecionado1['Hi Dir'].replace({'N': 0, 'NNE': 22.5, 'NE': 45.0, 'ENE': 67.5, 'E': 90.0, 'ESE': 112.5, 'SE': 135.0, 'SSE': 157.5, 'S': 180, 'SSW': 202.5, 'SW': 225.0, 'WSW': 247.5, 'W': 270, 'WNW': 292.5, 'NW': 315, 'NNW': 337.5})
    davis_selecionado1.loc[:, 'Wind Dir'] = davis_selecionado1['Wind Dir'].replace({'N': 0, 'NNE': 22.5, 'NE': 45.0, 'ENE': 67.5, 'E': 90.0, 'ESE': 112.5, 'SE': 135.0, 'SSE': 157.5, 'S': 180, 'SSW': 202.5, 'SW': 225.0, 'WSW': 247.5, 'W': 270, 'WNW': 292.5, 'NW': 315, 'NNW': 337.5})
    davis_selecionado1.loc[:, 'Hora'] = pd.to_datetime(davis_selecionado1['Hora'], format='%H:%M').dt.strftime('%H:%M')
    
        
    linha_ou_dispersao_1=st.radio('Escolha o tipo de Plotagem',['Linhas','Dispersão'])

    if linha_ou_dispersao_1 == 'Linhas':
        
        chart = alt.Chart(davis_selecionado1).mark_line().encode(
            x=alt.X('Hora:O', title='Hora do Dia'),
            y=alt.Y(f'{variavel_grafico}:Q', title=f'{variavel_grafico}'), 
            tooltip=['Hora', 'Temperatura:Q']
        ).properties(
            title=f'{variavel_grafico} ao longo do dia selecionado'
        )
        chart = chart.configure(background='white')  


        st.altair_chart(chart, use_container_width=True)
    if linha_ou_dispersao_1 == 'Dispersão':
        chart = alt.Chart(davis_selecionado1).mark_circle().encode(
            x=alt.X('Hora:O', title='Hora do Dia'),
            y=alt.Y(f'{variavel_grafico}:Q', title=f'{variavel_grafico}'), 
            tooltip=['Hora', 'Temperatura:Q']
        ).properties(
            title=f'{variavel_grafico} ao longo do dia selecionado'
        )

        st.altair_chart(chart, use_container_width=True)
        
plot_chuva=st.radio('Você deseja ver um Gráfico Setorial para Pluviometria de um dado ano',['Não','Sim'])
if plot_chuva == 'Sim':
    
    ano_selecionado = st.selectbox('Selecione o ano', anos_lista, index=0)

    davis_selecionado_ano = davis[davis['Year'] == ano_selecionado]

    precipitacao_por_mes = davis_selecionado_ano.groupby('Mês')['Precipitação'].sum().reset_index()

    total_precipitacao_ano = precipitacao_por_mes['Precipitação'].sum()

    precipitacao_por_mes['Proporcao'] = precipitacao_por_mes['Precipitação'] / total_precipitacao_ano * 100
    chart_rain = alt.Chart(precipitacao_por_mes).mark_arc().encode(
    theta=alt.Theta('Proporcao:Q', title='Proporção de Precipitação no Ano (%)'),
    color=alt.Color('Mês:O', scale=alt.Scale(scheme='accent'), title='Mês'),  
    tooltip=['Mês:O', 'Precipitação:Q', 'Proporcao:Q']
    ).properties(
        title=f'Distribuição da Precipitação no Ano {ano_selecionado}'
    )

    # Exibindo o gráfico no Streamlit
    st.altair_chart(chart_rain, use_container_width=True)








#aqui nos vamos fazer a parte que bota o gráfico de observações anuais  - analise 1

if anual_mensal == 'Anual':
    ano_analise1 = st.selectbox('Selecione o ano', anos_lista_analise_1, index=0, key='ano_analise1')
if anual_mensal == 'Mensal':
    ano_analise1 = st.selectbox('Selecione o ano', anos_lista_analise_1, index=0, key='ano_analise1')
    mes_analise=st.radio('Escolha um mês',['1','2','3','4','5','6','7','8','9','10','11','12'])
    mes_analise = int(mes_analise)
if anual_mensal == 'Anual' or anual_mensal == 'Mensal':
    med_min_max=st.radio('Escolha uma opção',['Média','Mínimo','Máximo'])

    n_variaveis=st.radio('Quantas variaveis para analisar',[1,2,3,4])
    conjunto_variaveis = []

    for i in range(n_variaveis):
        variavel = st.selectbox(f'Selecione a variável {i}', variaveis_analise1, key=f'var_{i}')
        conjunto_variaveis.append(variavel)

    if med_min_max == 'Média':
        med_min_max = 'mean'

    elif med_min_max == 'Mínimo':
        med_min_max = 'min'

    elif med_min_max == 'Máximo':
        med_min_max = 'max'

    # Criar um seletor de opções com radio buttons
    tab_or_graf = st.radio('Escolha uma opção:', ['Tabela', 'Gráfico'])

    davis_analise1=davis[davis['Year'] == ano_analise1]


    davis_analise1 = davis_analise1[['Year', 'Dat', 'Mês', 'Time', 'Dia'] + conjunto_variaveis]
    davis_analise1.loc[:, 'Hora'] = davis_analise1['Time']
    davis_analise1.loc[:, 'Hora'] = pd.to_datetime(davis_analise1['Hora'], format='%H:%M').dt.strftime('%H:%M')

    #Determinar como vai ser o df da analise
    # Aplicar a função estatística correta
    davis_analise1 = davis_analise1.groupby('Mês')[conjunto_variaveis].agg(med_min_max).reset_index()
    if anual_mensal == 'Mensal':
        davis_analise1 = davis[(davis['Year'] == ano_analise1) & (davis['Mês'] == int(mes_analise))]
        davis_analise1 = davis_analise1.groupby('Dia')[conjunto_variaveis].agg(med_min_max).reset_index()

    if tab_or_graf == 'Tabela':

        st.write(davis_analise1)

    elif tab_or_graf == 'Gráfico':
        variavel_analise1=conjunto_variaveis[0]    
        eixo_x = 'Mês' if anual_mensal == 'Anual' else 'Dia'

        
        if anual_mensal == 'Anual':
            line_or_scatter=st.radio('Tipo do Gráfico',['Linha','Dispersão','Colunas','Dispersão em ondas'])
        elif anual_mensal == 'Mensal':
            line_or_scatter=st.radio('Tipo do Gráfico',['Linha','Dispersão','Colunas'])


        for variavel_analise1 in conjunto_variaveis:

            if anual_mensal == 'Mensal':
                titulo_grafico = f'{variavel_analise1} ({med_min_max}) ao longo do período selecionado: {mes_analise}-{ano_analise1}'
            else:
                titulo_grafico = f'{variavel_analise1} ({med_min_max}) ao longo do período selecionado: {ano_analise1}'

            if line_or_scatter == 'Linha':
                chart2 = alt.Chart(davis_analise1).mark_line().encode(
                    x=alt.X(f'{eixo_x}:O', title=eixo_x),
                    y=alt.Y(
                        f'{variavel_analise1}:Q', 
                        title=f'{variavel_analise1}',  
                        scale=alt.Scale(domain=[davis_analise1[variavel_analise1].min(), davis_analise1[variavel_analise1].max()])
                    )
                ).properties(
                    title=titulo_grafico
                )
                st.altair_chart(chart2, use_container_width=True)

            elif line_or_scatter == 'Dispersão':
                chart2 = alt.Chart(davis_analise1).mark_circle().encode(
                    x=alt.X(f'{eixo_x}:O', title=eixo_x),
                    y=alt.Y(
                        f'{variavel_analise1}:Q', 
                        title=f'{variavel_analise1}',  
                        scale=alt.Scale(domain=[davis_analise1[variavel_analise1].min(), davis_analise1[variavel_analise1].max()])
                    )
                ).properties(
                    title=titulo_grafico
                )
                st.altair_chart(chart2, use_container_width=True)

            elif line_or_scatter == 'Colunas':
                chart2 = alt.Chart(davis_analise1).mark_bar(size=20).encode(
                    x=alt.X(f'{eixo_x}:N', title=eixo_x),
                    y=alt.Y(f'{variavel_analise1}:Q', title=f'{variavel_analise1}')
                ).properties(
                    title=titulo_grafico
                )
                st.altair_chart(chart2, use_container_width=True)
            elif line_or_scatter == 'Dispersão em ondas':
                davis_ano = davis[davis['Year'] == ano_analise1]

                davis_ano['Date'] = pd.to_datetime(davis_ano['Date'])
                step = 20
                overlap = 1

                chart_temp_ano = alt.Chart(davis_ano, height=step).transform_timeunit(
                    Month='month(Date)'
                ).transform_joinaggregate(
                    mean_value=f'mean({variavel_analise1})', groupby=['Month']
                ).transform_bin(
                    ['bin_max', 'bin_min'], variavel_analise1
                ).transform_aggregate(
                    value='count()', groupby=['Month', 'mean_value', 'bin_min', 'bin_max']
                ).transform_impute(
                    impute='value', groupby=['Month', 'mean_value'], key='bin_min', value=0
                ).mark_area(
                    interpolate='monotone',
                    fillOpacity=0.8,
                    stroke='lightgray',
                    strokeWidth=0.5
                ).encode(
                    alt.X('bin_min:Q')
                        .bin('binned')
                        .title(f'{variavel_analise1}'),
                    alt.Y('value:Q')
                        .axis(None)
                        .scale(range=[step, -step * overlap]),
                    alt.Fill('Month:N')  # Cada mês com cor diferente
                        .legend(None)
                        .scale(scheme='category20'),  # Paleta de cores distintas para meses
                ).facet(
                    row=alt.Row('Month:T')
                        .title(None)
                        .header(labelAngle=0, labelAlign='left', format='%B')
                ).properties(
                    title=f'{variavel_analise1} ao longo do ano {ano_analise1}',
                    bounds='flush'
                ).configure_facet(
                    spacing=0
                ).configure_view(
                    stroke=None
                ).configure_title(
                    anchor='end'
                )

                # Exibir o gráfico atualizado
                st.altair_chart(chart_temp_ano, use_container_width=True)
