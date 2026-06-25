import streamlit as st
import pandas as pd
import random
import requests # Biblioteca para fazer requisições à internet
import time
import base64  # Nosso ajudante para transformar a imagem em código secreto
import plotly.graph_objects as go

# 1. Configuração da página (Sempre a primeira linha de código!)
st.set_page_config(page_title="Simulador Copa 2026 - FIFA", page_icon="⚽", layout="wide")

# 2. FUNÇÃO SECRETA: Transforma o arquivo da imagem em texto para o site entender
def pegar_imagem_fundo(caminho_do_arquivo):
    with open(caminho_do_arquivo, "rb") as arquivo:
        dados_da_imagem = arquivo.read()
    codigo_secreto = base64.b64encode(dados_da_imagem).decode()
    return codigo_secreto

# Carrega o seu desenho do campo em aquarela
texto_da_imagem = pegar_imagem_fundo("campo_futebol.png")

# 3. A MAQUIAGEM DO SITE (VERSÃO FINAL COM CORREÇÃO DO MENU)
st.markdown(f"""
<style>
/* Coloca o campo de futebol bem no fundo do site */
.stApp {{
    background-image: url("data:image/png;base64,{texto_da_imagem}");
    background-size: cover;
    background-attachment: fixed;
    background-position: center;
}}

/* NOVO MÉTODO: Aplica o estilo de bloco escuro diretamente nos contêineres do Streamlit.
   Isso é mais robusto que injetar divs manualmente com st.markdown.
   O seletor procura por blocos verticais que contenham outros blocos verticais (a estrutura de um st.container com conteúdo). */
div[data-testid="stVerticalBlock"] > div:has(div[data-testid="stVerticalBlock"]) > div {{
    background-color: rgba(10, 10, 12, 0.90) !important;
    border-radius: 20px !important;
    padding: 25px !important;
    margin-bottom: 25px !important;
    box-shadow: 0px 8px 24px rgba(0, 0, 0, 0.6) !important;
    border: 1px solid rgba(255, 255, 255, 0.1) !important;

/* Nova estilização para os títulos dos Grupos (Centralizados e Maiores) */
h4 {{
    color: #FF1493 !important; /* Mantém o Rosa Choque marcante do projeto */
    font-family: 'Trebuchet MS', 'Impact', sans-serif !important;
    font-size: 2rem !important; /* Tamanho maior */
    text-align: center !important; /* Totalmente centralizado */
    text-transform: uppercase !important;
    letter-spacing: 1px !important;
    margin-top: 25px !important;
    margin-bottom: 15px !important;
    text-shadow: 1px 1px 3px rgba(0,0,0,0.5) !important;
}}




/* Títulos Maiores e de Auto Impacto */
/* TÍTULO PRINCIPAL (🏆 Arena de Dados...) */
h1 {{
    color: #FF1493 !important; /* Rosa Choque */
    font-family: 'Arial Black', sans-serif !important;
    text-transform: uppercase !important;
    font-size: 4.5rem !important; /* Aumentado para ser o maior destaque */
    text-shadow: 3px 3px 6px rgba(0,0,0,0.9) !important;
    margin-bottom: 20px !important;
    letter-spacing: 2px !important;
    text-align: center !important; /* Centraliza o título principal */
}} 

/* TÍTULOS DOS BLOCOS (📋 Grupos, 📊 Raio-X, 🎮 Simulador) */
h2 {{
    color: #00CED1 !important; /* Azul Turquesa */
    font-family: 'Arial Black', sans-serif !important;
    font-size: 2.3rem !important; /* Aumentado para dar destaque ao bloco */
    border-bottom: 3px solid #32CD32 !important; /* Linha Verde Limão mais grossa */
    padding-bottom: 12px !important;
    margin-top: 10px !important;
    margin-bottom: 20px !important;
    text-shadow: 2px 2px 4px rgba(0,0,0,0.8) !important;
}}

/* TÍTULOS INTERNOS DO SIMULADOR (📊 Probabilidades, 📝 Análise Tática, 🏅 Destaques) */
h3 {{ 
    color: #32CD32 !important; /* Verde Limão */
    font-family: 'Arial Black', sans-serif !important;
    font-size: 1.8rem !important; /* Aumentado para destacar o pós-jogo */
    margin-top: 25px !important;
    margin-bottom: 15px !important;
    text-shadow: 2px 2px 4px rgba(0,0,0,0.8) !important;
}}

/* Garante que os textos normais fiquem brancos e legíveis */
p, li, span, div, label {{ 
    color: #FFFFFF !important; 
    font-size: 1.1rem !important;
}}

/* Correção das opções do Selectbox para Azul Celeste e fundo Off-White */
div[data-baseweb="popover"] div,
div[data-baseweb="dropdown"] div,
div[data-baseweb="dropdown"] ul li,
div[role="listbox"] div,
div[role="listbox"] span,
.stSelectbox div[data-baseweb="select"] div {{
    color: #4FA8FF !important;
    font-weight: bold !important;
}}
div[data-baseweb="popover"], div[data-baseweb="dropdown"] ul {{
    background-color: #F8F9FA !important;
}}
/* Tabelas (Dataframes) modernas */
.stDataFrame {{
    background-color: #1E1E24 !important;
    border-radius: 12px;
    padding: 5px;
}}
/* Cores das letras internas e cabeçalhos em Azul Escuro */
div[data-testid="stDataFrame"] th, 
div[data-testid="stDataFrame"] td,
.stDataFrame div[role="columnheader"] span,
.stDataFrame div[role="gridcell"] {{
    color: #002060 !important;
    font-weight: bold !important;
}}

/* Efeito Zebrado Suave nas linhas das tabelas (Dois tons alternados) */
div[data-testid="stDataFrame"] tr:nth-child(odd) {{
    background-color: #F4F6F9 !important; /* Branco Gelo suave para as linhas ímpares */
}}

div[data-testid="stDataFrame"] tr:nth-child(even) {{
    background-color: #EBF3FA !important; /* Azul Pastel bem clarinho para as linhas pares */
}}
/* Ajuste fino para o zebrado das tabelas (garante que a cor preencha a célula inteira) */
div[data-testid="stDataFrame"] tr:nth-child(odd) td {{
    background-color: #F4F6F9 !important; 
}}
div[data-testid="stDataFrame"] tr:nth-child(even) td {{
    background-color: #EBF3FA !important;
}}
/* Botão Gamer em degradê */
.stButton>button {{
    background: linear-gradient(135deg, #FFD700 0%, #FF8C00 100%) !important;
    color: #000000 !important;
    border: none !important;
    font-weight: bold !important;
    padding: 12px 30px !important;
    border-radius: 10px !important;
}}
</style>
""", unsafe_allow_html=True)

# 4. CARREGANDO O BANCO DE DADOS (As 48 seleções)
@st.cache_data(ttl=600) # Mantém por 10 minutos para proteger seus créditos da API
def carregar_dados_da_api():
    url = "https://wc26-live-football-api.p.rapidapi.com/standings" # Ajustado para o endpoint de standings da nova API
    
    try:
        # Se a chave de API não estiver configurada nos segredos, usa o backup diretamente.
        if "RAPIDAPI_KEY" not in st.secrets or not st.secrets["RAPIDAPI_KEY"]:
            st.sidebar.warning("⚠️ Chave de API não configurada. Usando Backup Local.")
            return pd.read_csv("backup_times.csv")

        # A criação dos headers agora é feita APÓS a verificação do segredo
        headers = {
            "X-RapidAPI-Key": st.secrets["RAPIDAPI_KEY"],
            "X-RapidAPI-Host": st.secrets["RAPIDAPI_HOST"]
        }

        league_id = "1"
        season = "2022"
        rep_grupos = requests.get(url, headers=headers, params={"league": league_id, "season": season}, timeout=10)
        
        if rep_grupos.status_code == 200 and rep_grupos.json().get('response'):
            dados_grupos = rep_grupos.json()
            league_data = dados_grupos['response'][0]['league']
            lista_times = []
            
            for grupo_data in league_data['standings']:
                for time_info in grupo_data:
                    id_time = time_info['team']['id']
                    nome_time = time_info['team']['name']
                    grupo_letra = time_info['group'].replace("Group ", "")
                    ranking = time_info['rank']
                    
                    # Faz a requisição de scouts reais por time
                    # A nova API pode já incluir todos os dados, então a segunda chamada de 'stats' é removida.
                    # O código abaixo se torna um fallback caso os dados não venham na primeira chamada.
                    
                    # Valores padrão de contingência
                    gols_sofridos = time_info['all']['goals']['against']
                    amarelos = 2
                    faltas = 10
                    jogos = max(1, time_info['all']['played'])
                    chutes = 4 * jogos
                    passes = 400 * jogos
                    posse = 50
                    
                    # O bloco de stats foi simplificado, pois a nova API pode ter uma estrutura diferente.
                    # Mantemos a lógica de fallback com os dados já disponíveis no 'time_info'.
                    # Isso torna o código mais resiliente a mudanças na API.
                    amarelos = time_info.get('cards', {}).get('yellow', {}).get('total', amarelos)
                    chutes = time_info.get('all', {}).get('shots', {}).get('on', chutes)
                    passes = time_info.get('all', {}).get('passes', {}).get('total', passes)
                    faltas = time_info.get('all', {}).get('fouls', {}).get('committed', faltas)
                    
                    lista_times.append({
                        "Selecao": nome_time,
                        "Grupo": grupo_letra,
                        "RankingFifa": int(ranking),
                        "Passes_Completos": int(passes),
                        "Chutes_no_Alvo": int(chutes),
                        "Posse_Bola": int(posse),
                        "Gols_Sofridos": int(gols_sofridos),
                        "Cartoes_Amarelos": int(amarelos),
                        "Faltas": int(faltas)
                    })
            st.sidebar.success("🟢 Dados carregados da API externa!")
            return pd.DataFrame(lista_times)
        else:
            st.sidebar.warning(f"⚠️ API indisponível (Status: {rep_grupos.status_code}). Usando Backup Local.")
            return pd.read_csv("backup_times.csv")
            
    except Exception:
        st.sidebar.warning("⚠️ Modo Offline: Usando Banco de Dados Local.")
        return pd.read_csv("backup_times.csv")

# Executa a função para alimentar o aplicativo inteiro
df_times = carregar_dados_da_api()

# Título Principal do Painel
with st.container():
    st.markdown("<h1>🏆 Arena de Dados: Inteligência da Copa 2026</h1>", unsafe_allow_html=True)
    st.write("Bem-vindo ao seu centro de comando tático! Aqui, nós analisamos o histórico e o desempenho de cada seleção para tentar antecipar quem vai levantar a taça mais desejada do planeta.")

# 5. MOSTRANDO A TABELA DE GRUPOS (Cards envelopados com borda rosa)
with st.container():
    st.header("📋 Grupos Oficiais do Torneio") # O título foi mantido para consistência com o H2 do Raio-X
    grupos = sorted(df_times["Grupo"].unique()) # Ordena os grupos de A a L

    # Itera sobre os grupos em blocos de 3 para criar uma nova linha de colunas para cada bloco.
    # Isso garante a ordem A, B, C na primeira linha, D, E, F na segunda, e assim por diante.
    for i in range(0, len(grupos), 3):
        # Pega o bloco atual de até 3 grupos
        triade_grupos = grupos[i:i+3]
        # Cria 3 colunas para a linha atual
        cols = st.columns(3)
        # Itera sobre as colunas e os grupos do bloco atual
        for col, letra in zip(cols, triade_grupos):
            with col:
                times_do_grupo = df_times[df_times["Grupo"] == letra][["Selecao", "RankingFifa"]].sort_values(by='RankingFifa').reset_index(drop=True)
                st.markdown(f"<h4>📝 GRUPO {letra}</h4>", unsafe_allow_html=True)
                st.dataframe(
                    times_do_grupo,
                    hide_index=True,
                    use_container_width=True,
                    column_config={"Selecao": "Seleção", "RankingFifa": "Posição Ranking FIFA"}
                )

# 6. ABAS DE ANÁLISE DE DADOS (Dashboard Profissional)
with st.container():
    st.header("📊 Raio-X das Seleções")
    st.write("Quem tem o melhor futebol hoje? Abaixo, você confere o ranking de eficiência dos times com dados coletados diretamente do site oficial da FIFA. Use essas abas para analisar quem domina a posse de bola ou quem assusta mais o goleiro adversário!")

    aba_chutes, aba_passes, aba_defesa, aba_disciplina = st.tabs([
        "🎯 Líderes em Chutes ao Gol", 
        "👟 Mestres do Passe",
        "🛡️ Paredões da Defesa",
        "⚖️ Cartões e Disciplina"
    ])

    with aba_chutes:
        df_chutes = df_times[["Selecao", "Chutes_no_Alvo"]].sort_values(by="Chutes_no_Alvo", ascending=False).reset_index(drop=True)
        st.dataframe(df_chutes, hide_index=True, use_container_width=True, column_config={"Selecao": "Seleção", "Chutes_no_Alvo": "Chutes no Alvo"})

    with aba_passes:
        df_passes = df_times[["Selecao", "Passes_Completos"]].sort_values(by="Passes_Completos", ascending=False).reset_index(drop=True)
        st.dataframe(df_passes, hide_index=True, use_container_width=True, column_config={"Selecao": "Seleção", "Passes_Completos": "Passes Completos"})

    with aba_defesa:
        df_defesa = df_times.sort_values(by="Gols_Sofridos", ascending=True)[["Selecao", "Gols_Sofridos"]]
        st.dataframe(df_defesa, hide_index=True, use_container_width=True, column_config={"Selecao": "Seleção", "Gols_Sofridos": "Gols Sofridos"})

    with aba_disciplina:
        df_disciplina = df_times.sort_values(by="Cartoes_Amarelos", ascending=False)[["Selecao", "Cartoes_Amarelos", "Faltas"]]
        st.dataframe(df_disciplina, hide_index=True, use_container_width=True, column_config={"Selecao": "Seleção", "Cartoes_Amarelos": "Cartões Amarelos", "Faltas": "Faltas Cometidas"})


# PARTE FIXA 2: Histórico de Custos das Copas (Aparece sempre abaixo dos jogadores)
with st.container():
    st.header("💰 Histórico de Custos das Copas Modernas")
    st.write("""
    Os gastos totais com infraestrutura e organização das Copas do Mundo dispararam ao longo das últimas décadas. 
    Historicamente, não existem registros oficiais padronizados das primeiras edições (de 1930 até a década de 1980), 
    pois os custos eram baixos e focados em estádios isolados. Os dados consolidados ganharam relevância global a partir dos anos 1990.
    
    Confira abaixo a evolução dos custos estimados em **Bilhões de Dólares (USD)**:
    """)
    
    # Dados estruturados
    anos_sedes = [
        "1994<br>EUA", "1998<br>França", "2002<br>Japão/Coreia", "2006<br>Alemanha", 
        "2010<br>África do Sul", "2014<br>Brasil", "2018<br>Rússia", "2022<br>Catar", "2026<br>EUA/Can/Méx"
    ]
    custos = [0.5, 2.3, 7.0, 4.3, 3.6, 15.0, 11.6, 220.0, 14.0]
    
    # Cores personalizadas que remetem a cada país sede
    cores_paises = [
        '#0A3161', # 1994 EUA (Azul Marinho Americano)
        '#002395', # 1998 França (Azul Royal)
        '#0038A8', # 2002 Japão/Coreia (Azul/Vermelho)
        '#FFCC00', # 2006 Alemanha (Ouro/Preto)
        '#007A4D', # 2010 África do Sul (Verde)
        '#32CD32', # 2014 Brasil (Verde Limão/Amarelo)
        '#D52B1E', # 2018 Rússia (Vermelho)
        '#8A1538', # 2022 Catar (Vinho/Bordô do Catar)
        '#00A650'  # 2026 América do Norte (Verde/Azul/Vermelho integrado)
    ]
    
    # Criando o gráfico de linha funcional
    fig_custos = go.Figure()
    
    # Adiciona a linha principal (em tom cinza claro/branco para dar contraste)
    fig_custos.add_trace(go.Scatter(
        x=anos_sedes,
        y=custos,
        mode='lines+markers',
        line=dict(color='rgba(255, 255, 255, 0.4)', width=3),
        marker=dict(
            size=14,
            color=cores_paises, # Aplica a cor correspondente de cada país no ponto
            line=dict(color='white', width=2)
        ),
        text=[f"${c} Bi" for c in custos],
        textposition="top center",
        hoverinfo="text+x",
        showlegend=False
    ))
    
    # Customização do Layout para a interface escura do app
    fig_custos.update_layout(
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        margin=dict(t=20, b=40, l=40, r=20),
        height=380,
        xaxis=dict(
            tickmode='array',
            tickvals=anos_sedes,
            ticktext=anos_sedes,
            tickangle=-45,
            tickfont=dict(color="white", size=14, weight='bold'), # Aumentado para 14 e colocado em negrito para dar mais destaque
            gridcolor='rgba(255,255,255,0.05)'
        ),
        yaxis=dict(
            title=dict(text="Custo em Bilhões (USD)", font=dict(color="white")),
            tickfont=dict(color="white"),
            gridcolor='rgba(255,255,255,0.1)',
            type="linear" # Mantém a escala direta para chocar com a diferença do Catar
        )
    )
    
    # Exibe o gráfico na tela
    st.plotly_chart(fig_custos, use_container_width=True)

# PARTE FIXA 3: Linha do Tempo de Surpresas (Aparece sempre abaixo dos custos)
with st.container():
    st.header("⏳ Linha do Tempo: Top 5 Maiores Surpresas de 2026")
    st.write("""
    A fase de grupos da Copa do Mundo de 2026 entrou para a história como uma das edições mais equilibradas e imprevisíveis de todos os tempos. 
    Grandes potências mundiais foram travadas por defesas heroicas e organizações táticas impecáveis.
    
    Navegue na linha do tempo cronológica abaixo para relembrar as 5 maiores zebras e surpresas do torneio até aqui:
    """)
    
    # Dados estruturados cronologicamente (Rodada 1 à Classificação Antecipada)
    eventos = [
        "Portugal 1x1 RD Congo", 
        "Bélgica 1x1 Egito", 
        "Espanha 0x0 Cabo Verde", 
        "Uruguai 1x1 Arábia Saudita", 
        "Classificação da Noruega"
    ]
    
    # Datas fictícias sequenciais dentro de junho/2026 para marcar o eixo X
    datas = ["11/Jun", "13/Jun", "16/Jun", "19/Jun", "22/Jun"]
    
    # Textos descritivos completos para aparecerem no hover (passar o mouse)
    detalhes = [
        "Zebra na 1ª rodada: Portugal abriu o placar cedo, mas cedeu o empate à RD Congo, que somou seu 1º ponto na história das Copas.",
        "A badalada geração belga encontrou imensa dificuldade criativa e parou na forte organização tática da seleção egípcia.",
        "Partida heroica! O sistema defensivo de Cabo Verde segurou o poderoso ataque espanhol, frustrando os favoritos do grupo.",
        "O bicampeão Uruguai complicou-se severamente na tabela ao ceder o empate para os sauditas em jogo tenso.",
        "Surpresa positiva! Liderada pela consistência de Haaland, a Noruega garantiu vaga antecipada no mata-mata com autoridade."
    ]
    
    # Alturas alternadas no gráfico (Y) apenas para os balões não colidirem visualmente
    alturas = [1, -1, 1, -1, 1]
    
    # Criando o gráfico de linha do tempo
    fig_timeline = go.Figure()
    
    # 1. Linha do Eixo Central (Linha do Tempo)
    fig_timeline.add_trace(go.Scatter(
        x=datas,
        y=[0]*len(datas),
        mode='lines',
        line=dict(color='rgba(255, 255, 255, 0.3)', width=4),
        hoverinfo='skip',
        showlegend=False
    ))
    
    # 2. Linhas verticais que ligam os pontos ao eixo central
    for d, a in zip(datas, alturas):
        fig_timeline.add_trace(go.Scatter(
            x=[d, d],
            y=[0, a],
            mode='lines',
            line=dict(color='rgba(255, 255, 255, 0.15)', width=2, dash='dash'),
            hoverinfo='skip',
            showlegend=False
        ))
        
    # 3. Marcadores dos Eventos (Pontos em Rosa Choque, sem o texto flutuante)
    fig_timeline.add_trace(go.Scatter(
        x=datas,
        y=alturas,
        mode='markers', # MODO ALTERADO: Apenas os marcadores, o texto agora está nos balões fixos
        marker=dict(
            color='#FF1493',
            size=16,
            line=dict(color='white', width=2)
        ),
        hoverinfo='none', # Desativa o hover padrão, pois os balões são fixos
        showlegend=False
    ))
    
    # 4. CRIAÇÃO DOS BALÕES DE INFORMAÇÃO (ANNOTATIONS)
    baloes_fixos = []
    for d, a, ev, det in zip(datas, alturas, eventos, detalhes):
        posicao_y = 45 if a > 0 else -45
        
        baloes_fixos.append(dict(
            x=d,
            y=a,
            xref="x",
            yref="y",
            # Hierarquia de cores no texto: título em branco puríssimo e detalhe em cinza suave
            text=f"<b style='color:#FFFFFF; font-size:12px;'>{ev}</b><br><span style='color:#B0B3B8; font-size:10.5px; font-weight:normal;'>{det[:65]}...</span>",
            showarrow=True,
            arrowhead=0, # Remove a ponta da seta agressiva, deixando apenas uma linha guia minimalista
            arrowsize=1,
            arrowwidth=1,
            arrowcolor='rgba(255, 105, 180, 0.4)', # Linha guia rosa bem sutil e translúcida
            ax=0,
            ay=posicao_y * -1.3,
            font=dict(family="'Segoe UI', 'Helvetica Neue', sans-serif"),
            bgcolor="rgba(23, 23, 28, 0.92)", # Fundo escuro integrado perfeitamente ao painel
            bordercolor="rgba(255, 105, 180, 0.6)", # Borda rosa pastel fina e suave
            borderwidth=1,
            borderpad=8, # Mais espaçamento interno para o texto respirar
            align="center"
        ))
        
    # 5. Customização fina do layout para o painel escuro, agora com os balões
    fig_timeline.update_layout(
        annotations=baloes_fixos,
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        margin=dict(t=60, b=60, l=30, r=30),
        height=420,
        yaxis=dict(visible=False, range=[-3.5, 3.5]), # Amortecimento para os balões não cortarem
        xaxis=dict(
            tickfont=dict(color="#B0B3B8", size=11, weight='normal'), # Datas em tom cinza elegante
            gridcolor='rgba(0,0,0,0)', # CORREÇÃO: 'transparent' não é um valor válido para gridcolor. Usando o formato RGBA.
            linecolor='rgba(255,255,255,0.1)' # Linha do tempo horizontal bem discreta
        )
    )
    
    # Exibe o gráfico na tela
    st.plotly_chart(fig_timeline, use_container_width=True)

# 7. DESTAQUES INDIVIDUAIS (Layout Vertical e Cores Suaves)
with st.container():
    st.header("🏅 Destaques Individuais do Torneio")
    st.write("Confira o desempenho dos principais atletas de linha e os paredões que dominam as defesas nesta edição:")
    
    # --- GRÁFICO 1: JOGADORES (AGORA OCUPANDO A LARGURA TOTAL) ---
    st.markdown("<br><h5>🎯 Top 10 Jogadores (Gols e Assistências)</h5>", unsafe_allow_html=True)
    
    jogadores = ["Lionel Messi", "Kylian Mbappé", "Erling Haaland", "Michael Olise", "Vinícius Jr.", "Luis Díaz", "Harry Kane", "Bruno Fernandes", "Achraf Hakimi", "Pedri"]
    gols = [3, 4, 4, 1, 3, 2, 3, 1, 1, 1]
    assistencias = [2, 1, 0, 3, 2, 1, 1, 4, 2, 3]
    
    fig_jogadores = go.Figure()
    # Cores suavizadas em tons pastéis (Azul Mineral e Verde Sálvia)
    fig_jogadores.add_trace(go.Bar(x=jogadores, y=gols, name='Gols', marker_color='#7FA9D1'))
    fig_jogadores.add_trace(go.Bar(x=jogadores, y=assistencias, name='Assistências', marker_color='#A2C4A4'))
    
    fig_jogadores.update_layout(
        barmode='group',
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        margin=dict(t=15, b=30, l=40, r=20),
        height=320,
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1, font=dict(color="#B0B3B8", size=11)),
        xaxis=dict(
            tickfont=dict(color="#E4E6EB", size=12), # Letras retas, sem inclinação e fáceis de ler
            gridcolor='rgba(0,0,0,0)'
        ),
        yaxis=dict(
            title=dict(text="Quantidade", font=dict(color="#B0B3B8", size=11)),
            tickfont=dict(color="#B0B3B8"),
            range=[0, 5],
            dtick=1,
            gridcolor='rgba(255,255,255,0.05)'
        )
    )
    st.plotly_chart(fig_jogadores, use_container_width=True)
    
    st.markdown("<hr style='border-top: 1px solid rgba(255,255,255,0.05); margin: 25px 0;'>", unsafe_allow_html=True)
    
    # --- GRÁFICO 2: GOLEIROS (AGORA OCUPANDO A LARGURA TOTAL) ---
    st.markdown("<h5>🛡️ Top 10 Goleiros com Mais Defesas</h5>", unsafe_allow_html=True)
    
    goleiros = ["Alireza Beiranvand (Irã)", "Eloy Room (Curaçao)", "Vozinha (Cabo Verde)", "Lawrence Zigi (Gana)", "Mahmoud Abunada (Catar)", "B. Verbruggen (Holanda)", "Alisson (Brasil)", "D. Livaković (Croácia)", "Matt Freese (EUA)", "Edouard Mendy (Senegal)"]
    defesas = [46, 26, 25, 23, 20, 19, 19, 17, 14, 12]
    
    fig_goleiros = go.Figure()
    # Uma única cor Terracotta suave elegante para unificar o design corporativo
    fig_goleiros.add_trace(go.Bar(
        x=goleiros,
        y=defesas,
        name='Defesas',
        marker_color='#D98880',
        text=defesas, 
        textposition='outside',
        textfont=dict(color='#E4E6EB', size=11)
    ))
    
    fig_goleiros.update_layout(
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        margin=dict(t=25, b=30, l=40, r=20),
        height=320,
        showlegend=False,
        xaxis=dict(
            tickfont=dict(color="#E4E6EB", size=12), # Nomes inteiros na horizontal de forma limpa
            gridcolor='rgba(0,0,0,0)'
        ),
        yaxis=dict(
            title=dict(text="Total de Defesas", font=dict(color="#B0B3B8", size=11)),
            tickfont=dict(color="#B0B3B8"),
            gridcolor='rgba(255,255,255,0.05)'
        )
    )
    st.plotly_chart(fig_goleiros, use_container_width=True)

# 8. O CÉREBRO MATEMÁTICO (A lógica de quem vence o jogo)
def simular_jogo(time1, time2):
    dados_t1 = df_times[df_times["Selecao"] == time1].iloc[0]
    dados_t2 = df_times[df_times["Selecao"] == time2].iloc[0]
    
    # Cálculo do poder tático
    poder_t1 = (dados_t1["Passes_Completos"] / 100) + (dados_t1["Chutes_no_Alvo"] * 2) - (dados_t1["RankingFifa"] / 10)
    poder_t2 = (dados_t2["Passes_Completos"] / 100) + (dados_t2["Chutes_no_Alvo"] * 2) - (dados_t2["RankingFifa"] / 10)
    
    # Nova lógica de Empate baseada no equilíbrio (diferença de poder menor que 2)
    diferenca = abs(poder_t1 - poder_t2)
    if diferenca < 2:
        chance_empate = round(35 * (1 - (diferenca / 2))) # Até 35% de chance dependendo do equilíbrio
    else:
        chance_empate = max(5, round(20 - (diferenca * 2))) # Mínimo de 5% de chance residual de empate
        
    # Ajustando as porcentagens dos times descontando o empate
    min_poder = min(poder_t1, poder_t2)
    ajuste = abs(min_poder) + 1 if min_poder <= 0 else 0
    p1_ajustado = poder_t1 + ajuste
    p2_ajustado = poder_t2 + ajuste
    total_times = p1_ajustado + p2_ajustado
    
    restante = 100 - chance_empate
    chance_t1 = round((p1_ajustado / total_times) * restante)
    chance_t2 = restante - chance_t1
    
    # Determina o vencedor real (critério de desempate por posse se der igual na fórmula)
    if poder_t1 == poder_t2:
        vencedor = time1 if dados_t1["Posse_Bola"] > dados_t2["Posse_Bola"] else time2
    else:
        vencedor = time1 if poder_t1 > poder_t2 else time2
        
    return vencedor, chance_t1, chance_t2, chance_empate

# 8. ÁREA DO SIMULADOR (Interação do Usuário)
with st.container(): # O seletor CSS já estiliza este container automaticamente
    st.header("🎮 Simulador de Partidas")
    st.write("Escolha dois países para entrarem em campo. Nossa inteligência vai cruzar o volume de passes, a precisão dos chutes e o posicionamento no ranking para rodar 90 minutos de jogo matemáticos. Quem sairá vencedor?")
    lista_selecoes = df_times["Selecao"].tolist()

    c1, c2 = st.columns(2)
    with c1:
        time_a = st.selectbox("Escolha a Seleção A", lista_selecoes, index=8) # Começa no Brasil
    with c2:
        time_b = st.selectbox("Escolha a Seleção B", lista_selecoes, index=32) # Começa na França

    if st.button("🔥 Apitar Início da Partida!"):
        if time_a == time_b:
            st.warning("Jogo inválido! Escolha duas seleções diferentes para competir.")
        else:
            vencedor, chance_a, chance_b, chance_empate = simular_jogo(time_a, time_b)
            
            time_perdedor = time_b if vencedor == time_a else time_a
            dados_vencedor = df_times[df_times["Selecao"] == vencedor].iloc[0]
            dados_perdedor = df_times[df_times["Selecao"] == time_perdedor].iloc[0]
            
            st.balloons()
            st.success(f"🎉 Fim de papo na arena de dados! O grande vencedor é: **{vencedor}**!")
            
            st.write("### 📊 Probabilidades Iniciais do Confronto:")
            
            # CORES COM ALTO CONTRASTE (Verde Vivo para Vencedor, Amarelo Ouro para Perdedor)
            cor_time_a = '#2ECC71' if vencedor == time_a else '#F1C40F'
            cor_time_b = '#2ECC71' if vencedor == time_b else '#F1C40F'
            
            # Bolinhas da legenda dinâmicas
            bola_time_a = '🟢' if vencedor == time_a else '🟡'
            bola_time_b = '🟢' if vencedor == time_b else '🟡'

            # Criando duas colunas para colocar os gráficos lado a lado
            col_grafico1, col_grafico2 = st.columns(2)
            
            with col_grafico1:
                st.write("##### 🔮 Chances de Vitória")
                fig_pie = go.Figure(data=[go.Pie(
                    labels=[time_a, time_b], 
                    values=[chance_a, chance_b], 
                    hole=.6, 
                    marker=dict(colors=[cor_time_a, cor_time_b]),
                    textinfo='percent',
                    textfont=dict(size=14, color='white', weight='bold'),
                    showlegend=False
                )])
                fig_pie.update_layout(
                    paper_bgcolor='rgba(0,0,0,0)',
                    plot_bgcolor='rgba(0,0,0,0)',
                    margin=dict(t=10, b=10, l=10, r=10),
                    height=200
                )
                st.plotly_chart(fig_pie, use_container_width=True)
                
            with col_grafico2:
                st.write("##### 🤝 Probabilidade de Empate")
                # Gráfico de Velocímetro com a barra em Azul Claro Elétrico (#00D2FF)
                fig_gauge = go.Figure(go.Indicator(
                    mode = "gauge+number",
                    value = chance_empate,
                    number = {'suffix': "%", 'font': {'color': "white", 'size': 24, 'weight': 'bold'}},
                    domain = {'x': [0, 1], 'y': [0, 1]},
                    gauge = {
                        'axis': {'range': [0, 100], 'tickwidth': 1, 'tickcolor': "white"},
                        'bar': {'color': "#00D2FF"}, # Azul para o Empate
                        'bgcolor': "rgba(255,255,255,0.1)",
                        'borderwidth': 2,
                        'bordercolor': "white",
                    }
                ))
                fig_gauge.update_layout(
                    paper_bgcolor='rgba(0,0,0,0)',
                    plot_bgcolor='rgba(0,0,0,0)',
                    margin=dict(t=30, b=10, l=10, r=10),
                    height=200
                )
                st.plotly_chart(fig_gauge, use_container_width=True)
                
            # Legendas atualizadas com as cores novas
            st.write(f"{bola_time_a} **{time_a}**: {chance_a}% de chance de vitória")
            st.write(f"{bola_time_b} **{time_b}**: {chance_b}% de chance de vitória")
            st.write(f"🔵 **Probabilidade de Empate**: {chance_empate}%")
            
            # Análise tática explicativa humana
            st.write("### 📝 Análise Tática dos Nossos Analistas:")
            motivos = []
            if dados_vencedor["Chutes_no_Alvo"] > dados_perdedor["Chutes_no_Alvo"]:
                motivos.append(f"agressividade no ataque, finalizando mais vezes direto no alvo ({dados_vencedor['Chutes_no_Alvo']} contra {dados_perdedor['Chutes_no_Alvo']})")
            if dados_vencedor["Passes_Completos"] > dados_perdedor["Passes_Completos"]:
                motivos.append(f"maior precisão na troca de passes e na construção de jogadas ({dados_vencedor['Passes_Completos']} contra {dados_perdedor['Passes_Completos']})")
            if dados_vencedor["RankingFifa"] < dados_perdedor["RankingFifa"]:
                motivos.append("maior peso e experiência internacional refletidos na sua posição superior no ranking mundial da FIFA")
                
            if motivos:
                explicacao = f"A vitória do **{vencedor}** foi construída principalmente devido à sua " + " e ".join(motivos) + "."
            else:
                explicacao = f"Foi um jogo equilibradíssimo, decidido nos detalhes táticos e no controle da posse de bola no meio de campo!"
                
            st.info(explicacao)