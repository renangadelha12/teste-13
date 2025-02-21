import streamlit as st
import pandas as pd
import plotly.express as px
import altair as alt
import streamlit as st
st.set_page_config(page_title="Dashboard de Dados Meteorológicos", layout="wide")
st.markdown('<h1 style="color:orange">Dashboard de Dados Meteorológicos - Vantage Pro 2</h1>', unsafe_allow_html=True)

temas=st.radio('Escolha um Tema',['Padrão','Escuro','INPE'])
# Alternador de tema

# Configuração de cores para os temas
if temas == 'Escuro':
    bg_color = "#121212"       # Fundo escuro
    text_color = "#FFA500"      # Texto laranja no modo escuro
    card_bg = "#1e1e1e"        # Cartões mais escuros
    bar_color = "#FFA500"      # Cor das barras no gráfico
    chart_bg = "#2a2a2a"       # Fundo grafite dos gráficos
    border_color=text_color
    selected_bg = "orange"  # Cor de fundo quando selecionado
    selected_text = "#333333"  # Cor do texto quando selecionado
        

elif temas == 'Padrão':
    bg_color = "#ffffff"       # Fundo branco
    text_color = "#5c8aff"      # Texto preto no modo claro
    card_bg = "#f5f5f5"        # Cartões mais claros
    bar_color = "#5c8aff"      # Cor das barras no gráfico
    chart_bg = "#ffffff"       # Fundo branco dos gráficos
    border_color=text_color
    selected_bg = "#007BFF"  # Cor de fundo quando selecionado
    selected_text = "white"
elif temas == 'INPE':
    bg_color = "#0078BE"       # Fundo 
    text_color = "#FF9300"      # Texto 
    card_bg = "#0078BE"        # Cartões 
    bar_color = "#FFA500"      # Cor das barras no gráfico
    chart_bg = "#0078BE"       # Fundo branco dos gráficos
    border_color=text_color
    selected_bg = "#007BFF"  # Cor de fundo quando selecionado
    selected_text = "0078BE"






# Definição de CSS para os temas (garantindo que o texto fique laranja no modo escuro)
tema_css = f"""
<style>
.stApp {{
    background-color: {bg_color};
    color: {text_color};
}}
h1, h2, h3, h4, h5, h6, p, span, div {{
    color: {text_color} !important;
}}
.main {{
    max-width: 85%;
    margin: 0 auto;
    padding: 20px;
    border-radius: 10px;
    background-color: {card_bg};
    box-shadow: 2px 2px 10px rgba(0, 0, 0, 0.2);
}}
</style>
"""
selectbox_css = f"""

<style>
div[data-baseweb="select"] {{
    background-color: {card_bg} !important; /* Fundo do dropdown */
    color: {text_color} !important; /* Cor do texto */
    border-radius: 5px;
}}

div[data-baseweb="select"] > div {{
    background-color: {card_bg} !important; /* Fundo da caixa de opções */
}}
</style>
"""

selectradio_css = f"""
<style>
/* Estilos para os botões de rádio */
div[data-baseweb="radio"] {{
    background-color: {card_bg} !important; /* Fundo do contêiner */
    color: {text_color} !important; /* Cor do texto */
    border-radius: 5px;
    padding: 10px;
}}

div[data-baseweb="radio"] label {{
    color: {text_color} !important; /* Cor do texto das labels */
}}

div[data-baseweb="radio"] div[role="radio"] {{
    background-color: {card_bg} !important; /* Fundo dos botões de rádio */
    color: {text_color} !important; /* Cor do texto do botão */
    border: 2px solid {border_color} !important; /* Borda do botão */
    padding: 5px 15px;
    border-radius: 5px;
    margin-bottom: 5px;
    transition: background-color 0.3s, color 0.3s !important;
}}

div[data-baseweb="radio"] div[role="radio"]:hover {{
    background-color: {border_color} !important; /* Fundo no hover */
    color: {card_bg} !important; /* Cor do texto no hover */
}}

div[data-baseweb="radio"] div[role="radio"][aria-checked="true"] {{
    background-color: {selected_bg} !important; /* Fundo quando selecionado */
    color: {selected_text} !important; /* Cor do texto quando selecionado */
    border: 2px solid {selected_bg} !important; /* Borda quando selecionado */
}}

div[data-baseweb="radio"] div[role="radio"]:not([aria-checked="true"]) {{
    background-color: {card_bg} !important; /* Fundo para os não selecionados */
    color: {text_color} !important;
}}

</style>
"""

# Inserir o CSS no Streamlit
st.markdown(selectradio_css, unsafe_allow_html=True)
st.markdown(selectbox_css, unsafe_allow_html=True)

# Aplicação do tema dinâmico
st.markdown(tema_css, unsafe_allow_html=True)
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
            tooltip=['Hora', 'Temperatura:Q'],
            color=alt.value(bar_color)
        ).properties(
        title=f'{variavel_grafico} ao longo do dia selecionado',
        background=chart_bg,
    ).configure_title(
        fontSize=20,
        color=text_color  # Define a cor do título
    ).configure_view(
        strokeWidth=0  # Remove borda ao redor do gráfico
    ).configure_axis(
        labelColor=text_color,  # Cor dos rótulos dos eixos
        titleColor=text_color  # Cor dos títulos dos eixos
    )  


        st.altair_chart(chart, use_container_width=True)
    if linha_ou_dispersao_1 == 'Dispersão':
        chart = alt.Chart(davis_selecionado1).mark_circle().encode(
            x=alt.X('Hora:O', title='Hora do Dia'),
            y=alt.Y(f'{variavel_grafico}:Q', title=f'{variavel_grafico}'), 
            tooltip=['Hora', 'Temperatura:Q'],
            color=alt.value(bar_color)
        ).properties(
            title=f'{variavel_grafico} ao longo do dia selecionado',
            background=chart_bg,
        ).configure_title(
            fontSize=20,
            color=text_color  # Define a cor do título
        ).configure_view(
            strokeWidth=0  # Remove borda ao redor do gráfico
        ).configure_axis(
            labelColor=text_color,  # Cor dos rótulos dos eixos
            titleColor=text_color  # Cor dos títulos dos eixos
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
                    title=f'Distribuição da Precipitação no Ano {ano_selecionado}',
                    background=chart_bg,
                ).configure_title(
                    fontSize=20,
                    color=text_color  # Define a cor do título
                ).configure_view(
                    strokeWidth=0  # Remove borda ao redor do gráfico
                ).configure_axis(
                    labelColor=text_color,  # Cor dos rótulos dos eixos
                    titleColor=text_color  # Cor dos títulos dos eixos
                )

    # Exibindo o gráfico no Streamlit
    st.altair_chart(chart_rain, use_container_width=True)








#aqui nos vamos fazer a parte que bota o gráfico de observações anuais  - analise 1



if anual_mensal == 'Anual' or anual_mensal == 'Mensal':
    med_min_max=st.radio('Escolha uma opção',['Média','Mínimo','Máximo'])
    n_variaveis = st.radio('Quantas variáveis para analisar', [1, 2, 3, 4])
    conjunto_variaveis = []
    variaveis_disponiveis = variaveis_analise1.copy()  # Faz uma cópia da lista original

    for i in range(n_variaveis):
        if not variaveis_disponiveis:
            break  # Para o loop se não houver mais variáveis disponíveis

        variavel = st.selectbox(f'Selecione uma variável ', variaveis_disponiveis, key=f'var_{i}')
        conjunto_variaveis.append(variavel)

        # Remove a variável selecionada da lista disponível
        variaveis_disponiveis.remove(variavel)

    if med_min_max == 'Média':
        med_min_max = 'mean'

    elif med_min_max == 'Mínimo':
        med_min_max = 'min'

    elif med_min_max == 'Máximo':
        med_min_max = 'max'

    # Criar um seletor de opções com radio buttons
    tab_or_graf = st.radio('Escolha uma opção:', ['Tabela', 'Gráfico'])
    

# Supondo que 'davis' seja o DataFrame contendo os dados e as listas de anos e variáveis disponíveis
if anual_mensal == 'Anual':
    #n_anos = st.radio('Quantos anos você quer analisar', [1, 2, 3, 4])
    n_years = st.number_input(
        'Quantos anos você quer analisar?', 
        min_value=1,  
        step=1,  
        value=1  
    )
    n_anos=int(n_years)
    conjunto_anos = []
    anos_disponiveis = anos_lista_analise_1.copy()
    cols = st.columns(n_anos)

    for i in range(n_anos):
        if not anos_disponiveis:
            break
        with cols[i]:  # Coloca o selectbox dentro da coluna correspondente
            ano = st.selectbox(f'Ano ', anos_disponiveis, key=f'ano_{i}')
        conjunto_anos.append(ano)
        anos_disponiveis.remove(ano)

    if len(conjunto_anos) == 1:
        ano_analise1 = conjunto_anos[0]
        davis_analise1 = davis[davis['Year'] == ano_analise1]
        davis_analise1 = davis_analise1[['Year', 'Dat', 'Mês', 'Time', 'Dia'] + conjunto_variaveis]

        davis_analise1['Hora'] = pd.to_datetime(davis_analise1['Time'], format='%H:%M').dt.strftime('%H:%M')

        davis_analise1 = davis_analise1.groupby('Mês')[conjunto_variaveis].agg(med_min_max).reset_index()

    elif len(conjunto_anos) > 1:
        davis_analise2 = davis[davis['Year'].isin(conjunto_anos)]
        davis_analise2 = davis_analise2[['Year', 'Dat', 'Mês', 'Time', 'Dia'] + conjunto_variaveis]
        davis_analise2 = davis_analise2.groupby(['Mês', 'Year'])[conjunto_variaveis].agg(med_min_max).reset_index()



    # Escolha de Tabela ou Gráfico
    if tab_or_graf == 'Tabela':
        if len(conjunto_anos) == 1:
            st.write(davis_analise1)
        else:
            st.write(davis_analise2)

    elif tab_or_graf == 'Gráfico':
        variavel_analise1 = conjunto_variaveis[0]    
        eixo_x = 'Mês' if anual_mensal == 'Anual' else 'Dia'

        if anual_mensal == 'Anual':
            line_or_scatter = st.radio('Tipo do Gráfico', ['Linha', 'Dispersão', 'Colunas'])
        else:
            line_or_scatter = st.radio('Tipo do Gráfico', ['Linha', 'Dispersão', 'Colunas'])

        for variavel_analise1 in conjunto_variaveis:
            titulo_grafico = f'{variavel_analise1} ({med_min_max}) ao longo do período selecionado'

            if len(conjunto_anos) == 1:
                df_plot = davis_analise1
            else:
                df_plot = davis_analise2

            if line_or_scatter == 'Linha':
                chart = alt.Chart(df_plot).mark_line().encode(
                    x=alt.X(f'{eixo_x}:O', title=eixo_x),
                    y=alt.Y(f'{variavel_analise1}:Q', title=variavel_analise1,scale=alt.Scale(domain=[df_plot[variavel_analise1].min(), df_plot[variavel_analise1].max()])),
                    color='Year:N' if len(conjunto_anos) > 1 else alt.value(bar_color)
                ).properties(
                    title=titulo_grafico,
                    background=chart_bg,
                ).configure_axis(
                    labelColor=text_color,  
                    titleColor=text_color  
                )
                st.altair_chart(chart, use_container_width=True)

            elif line_or_scatter == 'Dispersão':
                chart = alt.Chart(df_plot).mark_circle().encode(
                    x=alt.X(f'{eixo_x}:O', title=eixo_x),
                    y=alt.Y(f'{variavel_analise1}:Q', title=variavel_analise1,scale=alt.Scale(domain=[df_plot[variavel_analise1].min(), df_plot[variavel_analise1].max()])),
                    color='Year:N' if len(conjunto_anos) > 1 else alt.value(bar_color)
                ).properties(
                    title=titulo_grafico,
                    background=chart_bg,
                ).configure_axis(
                    labelColor=text_color,  
                    titleColor=text_color  
                )
                st.altair_chart(chart, use_container_width=True)

            elif line_or_scatter == 'Colunas':
                chart = alt.Chart(df_plot).mark_bar(size=20).encode(
                    x=alt.X(f'{eixo_x}:O', title=eixo_x),
                    y=alt.Y(f'{variavel_analise1}:Q', title=variavel_analise1),
                    color='Year:N' if len(conjunto_anos) > 1 else alt.value(bar_color)
                ).properties(
                    title=titulo_grafico,
                    background=chart_bg,
                ).configure_axis(
                    labelColor=text_color,  
                    titleColor=text_color  
                )
                st.altair_chart(chart, use_container_width=True)

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
                        bounds='flush',
                        background=chart_bg
                    ).configure_facet(
                        spacing=0
                    ).configure_view(
                        stroke=None
                    ).configure_title(
                        anchor='end'
                    )

                    # Exibir o gráfico atualizado
                    st.altair_chart(chart_temp_ano, use_container_width=True)
if anual_mensal == 'Mensal':
    n_years = st.number_input(
        'Quantos anos você quer analisar?', 
        min_value=1,  
        step=1,  
        value=1  
    )
    n_anos=int(n_years)
    conjunto_anos = []
    anos_disponiveis = anos_lista_analise_1.copy()
    cols = st.columns(n_anos)

    for i in range(n_anos):
        if not anos_disponiveis:
            break
        with cols[i]:  # Coloca o selectbox dentro da coluna correspondente
            ano = st.selectbox(f'Ano ', anos_disponiveis, key=f'ano_{i}')
        conjunto_anos.append(ano)
        anos_disponiveis.remove(ano)

    # Selecionar os meses desejados
    meses_disponiveis = list(range(1, 13))  # Janeiro (1) a Dezembro (12)
    conjunto_meses = st.multiselect('Selecione os meses para análise', meses_disponiveis)

    if conjunto_anos and conjunto_meses:
        # Filtrar os dados para os anos e meses selecionados
        davis_analise = davis[(davis['Year'].isin(conjunto_anos)) & (davis['Mês'].isin(conjunto_meses))]

        # Agrupar por Dia, Mês e Ano
        davis_analise = davis_analise.groupby(['Dia', 'Mês', 'Year'])[conjunto_variaveis].agg(med_min_max).reset_index()

        # Criar coluna de rótulo para o eixo X (Dia do mês)
        davis_analise['Dia_Mês'] = davis_analise['Dia'].astype(str)

        # Exibir tabela se necessário
        if tab_or_graf == 'Tabela':
            st.write(davis_analise)

        # Criar gráfico
        elif tab_or_graf == 'Gráfico':
            line_or_scatter_m = st.radio('Tipo do Gráfico', ['Linha', 'Dispersão'])
            variavel_analise1 = conjunto_variaveis

            for i in range(len(conjunto_variaveis)):
                titulo_grafico = f"Comparação diária entre anos diferentes - {variavel_analise1[i]}"

                if line_or_scatter_m == 'Linha':
                    chart = alt.Chart(davis_analise).mark_line(point=True).encode(
                        x=alt.X("Dia:O", title="Dia do Mês"),
                        y=alt.Y(f"{variavel_analise1[i]}:Q", title=variavel_analise1[i],scale=alt.Scale(domain=[davis_analise[variavel_analise1].min().item(), davis_analise[variavel_analise1].max().item()])),
                        color=alt.Color("Year:N", title="Ano"),
                    ).properties(
                        title=titulo_grafico,
                        background=chart_bg
                    ).configure_title(
                        fontSize=20,
                        color=text_color
                    ).configure_axis(
                        labelColor=text_color,
                        titleColor=text_color
                    )

                elif line_or_scatter_m == 'Dispersão':
                    chart = alt.Chart(davis_analise).mark_circle(size=100, opacity=0.9).encode(
                        x=alt.X("Dia:O", title="Dia do Mês"),
                        y=alt.Y(f"{variavel_analise1[i]}:Q", title=variavel_analise1[i]),
                        color=alt.Color("Year:N", title="Ano"),
                    ).properties(
                        title=titulo_grafico,
                        background=chart_bg
                    ).configure_title(
                        fontSize=20,
                        color=text_color
                    ).configure_axis(
                        labelColor=text_color,
                        titleColor=text_color
                    )

             

               
                st.altair_chart(chart, use_container_width=True)


            

            
