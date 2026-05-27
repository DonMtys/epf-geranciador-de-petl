import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Jogos LC 840/2011",
    page_icon="🎮",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Remove padding e barra do Streamlit
st.markdown("""<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}
.block-container {padding-top: 1rem !important; padding-bottom: 0 !important;}
section[data-testid="stSidebar"] {min-width: 200px; max-width: 220px;}
</style>""", unsafe_allow_html=True)

JOGOS = {
    "🏠 Hub — Todos os jogos":       "jogos_lc840.html",
    "🧩 Quiz LC 840":                "quiz_lc840.html",
    "⏱️ Jogo dos Prazos":           "prazos_lc840.html",
    "🃏 Flashcards":                 "flashcards_lc840.html",
    "📋 Quiz Questões Reais":        "quiz_real_lc840.html",
    "🧠 Jogo da Memória":            "memoria_lc840.html",
    "⚡ Speed Round":                "speed_lc840.html",
    "💀 Modo Sobrevivência":         "survival_lc840.html",
    "✏️ Complete a Frase":           "complete_lc840.html",
    "📚 App de Estudos (estudo.html)":"estudo.html",
}

with st.sidebar:
    st.markdown("### 🎮 LC 840/2011")
    st.markdown("---")
    jogo = st.radio("Selecione o jogo:", list(JOGOS.keys()), label_visibility="collapsed")

html_file = JOGOS[jogo]
with open(html_file, "r", encoding="utf-8") as f:
    html_content = f.read()

components.html(html_content, height=820, scrolling=True)
