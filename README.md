# 🏆 Arena de Dados: Inteligência da Copa 2026

![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=Streamlit&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Plotly](https://img.shields.io/badge/Plotly-3F4F75?style=for-the-badge&logo=Plotly&logoColor=white)

Uma aplicação interativa de Business Intelligence e Ciência de Dados voltada para a **Copa do Mundo de 2026**. O ecossistema analisa dados estruturados de 48 seleções divididas em 12 grupos oficiais, fornecendo inteligência competitiva, análises táticas integradas e acompanhamento histórico-financeiro das Copas modernas.

---

## 🚀 Funcionalidades Principais

* **Painel Geral de Grupos:** Grid responsivo de 12 grupos (A a L) ordenados de forma tática pelo Rank oficial da FIFA, apresentando layouts customizados de tabelas zebradas para máxima legibilidade.
* **Raio-X das Seleções:** Abas interativas segmentadas em scouts de desempenho (*Líderes em Chutes ao Gol*, *Mestres do Passe*, *Paredões da Defesa* e *Cartões e Disciplina*).
* **Destaques Individuais (Top 10):** Gráficos de barras verticais limpos e empilhados para análise comparativa contendo a relação de gols/assistências e o ranking isolado de defesas dos goleiros em tons pastéis e corporativos.
* **Análise Econômica Histórica:** Gráfico evolutivo demonstrando o impacto financeiro e orçamentário em bilhões de dólares das Copas do Mundo desde 1994.
* **Linha do Tempo Interativa (Timeline):** Infográfico dinâmico mapeando as 5 maiores surpresas e zebras registradas na fase de grupos do torneio com anotações fixas e micro-copy estilizado.
* **Arquitetura de Contingência Sem Falhas (Modo Offline):** Caso o limite de requisições da API externa seja atingido, a aplicação migra automaticamente para um banco de dados local estruturado (`backup_times.csv`), mantendo o painel 100% operacional.

---

## 🛠️ Tecnologias e Bibliotecas Utilizadas

A aplicação foi inteiramente desenvolvida em **Python**, utilizando as seguintes bibliotecas e componentes:

* **`streamlit` (`st`):** Framework principal utilizado para a construção e renderização da interface web reativa e gerenciamento de estado.
* **`pandas` (`pd`):** Manipulação, tratamento, filtragem e estruturação matricial dos dados dos grupos e seleções.
* **`plotly.graph_objects` (`go`):** Desenvolvimento de gráficos customizados de alta performance com injeção de layouts escuros, anotações e barras agrupadas.
* **`requests`:** Consumo de APIs rest externas via requisições HTTP assíncronas monitoradas por blocos de tratamento (`try-except`).
* **`time`:** Otimização do fluxo de consultas através de pausas táticas (`time.sleep`), respeitando os limites de *Rate Limit* da API do plano gratuito.
* **`base64`:** Processamento local e decodificação binária de imagens de background (customização do campo de futebol) diretamente nas regras CSS.
* **`random`:** Lógicas auxiliares de aleatoriedade matemática.

---

## 🎨 UI/UX & Identidade Visual

O design contorna os limites padrões do framework utilizando injeções de **HTML5 e CSS3 customizados** (`unsafe_allow_html=True`):
* **Tipografia e Títulos:** Título do painel principal maximizado via tags estruturais `<h1>` com sombras projetadas, garantindo imponência ao projeto.
* **Tabelas Minimalistas:** Remoção de índices padrões e estilização de linhas alternadas nas tabelas internas utilizando paletas de cores pastéis suavizadas (Branco Gelo `#F4F6F9` e Azul Pastel `#EBF3FA`) com fontes em Azul Escuro (`#002060`) para contraste ideal de leitura.
* **Gráficos Elegantes:** Substituição de cores supersaturadas por paletas sóbrias (Azul Mineral, Verde Sálvia e Terracotta), mantendo o foco analítico e a consistência corporativa.

---

## 🏁 Como Executar o Projeto Localmente

### 1. Clonar o Repositório
```bash
git clone [https://github.com/Emiliabz/projeto_copa_2026.git](https://github.com/Emiliabz/projeto_copa_2026.git)
cd projeto_copa_2026