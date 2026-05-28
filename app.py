from pathlib import Path

import streamlit as st
import streamlit.components.v1 as components


BASE_DIR = Path(__file__).parent

JOGOS = {
    "Hub - Todos os jogos": "jogos_lc840.html",
    "Quiz LC 840": "quiz_lc840.html",
    "Jogo dos Prazos": "prazos_lc840.html",
    "Flashcards": "flashcards_lc840.html",
    "Quiz Questoes Reais": "quiz_real_lc840.html",
    "Jogo da Memoria": "memoria_lc840.html",
    "Speed Round": "speed_lc840.html",
    "Modo Sobrevivencia": "survival_lc840.html",
    "Complete a Frase": "complete_lc840.html",
    "App de Estudos": "estudo.html",
    "Gestao de Estoques": "gestao_estoques.html",
}


st.set_page_config(
    page_title="Jogos LC 840/2011",
    page_icon="LC",
    layout="wide",
    initial_sidebar_state="collapsed",
)

st.markdown(
    """
    <style>
    #MainMenu, footer, header {visibility: hidden;}
    .block-container {
        max-width: 980px;
        padding: 0.65rem 0.65rem 0 !important;
    }
    div[data-testid="stSelectbox"] {
        max-width: 520px;
        margin: 0 auto 0.55rem auto;
    }
    div[data-testid="stSelectbox"] label {
        font-size: 0.9rem;
        font-weight: 700;
    }
    iframe {
        width: 100% !important;
        border: 0 !important;
        border-radius: 0 !important;
    }
    @media (max-width: 640px) {
        .block-container {
            padding-left: 0.35rem !important;
            padding-right: 0.35rem !important;
        }
        div[data-testid="stSelectbox"] {
            margin-bottom: 0.35rem;
        }
    }
    </style>
    """,
    unsafe_allow_html=True,
)

jogo = st.selectbox(
    "Escolha o jogo",
    options=list(JOGOS.keys()),
    index=list(JOGOS.keys()).index("Modo Sobrevivencia"),
)

html_path = BASE_DIR / JOGOS[jogo]

if not html_path.exists():
    st.error(f"Arquivo nao encontrado: {html_path.name}")
    st.stop()

html_content = html_path.read_text(encoding="utf-8")
components.html(html_content, height=880, scrolling=True)
