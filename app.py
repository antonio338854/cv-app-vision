import streamlit as
st
ctonl as op
1from PIL import Image
import pandas as pd
from io import BytesIO
from vision_processor import VisionProcessor
import os
from datetime import datetime

# Configuração da página
st.set_page_config(
    page_title="Vision Computacional App",
    page_icon="🐄",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Estilo CSS personalizado
st.markdown(```
    <style>
    .main-header {
        font-size: 3em;
        color: #1f77b4;
        text-align: center;
        margin-bottom: 2rem;
    }
    .section-header {
        font-size: 1.8em;
        color: #ff7f0e;
        margin: 1.5rem 0 1rem 0;
        border-bottom: 2px solid #1f77b4;
        padding-bottom: 0.5rem;
    }
    </style>
```, unsafe_allow_html=True)

# Título da aplicação
st.markdown('<div class="main-header"��$��$욪�ão Computacional Pron</div>', unsafe_allow_html=True)

# Inicializar+ processador de visão
@st.cache_resource
def get_processor():
    return VisionProcessor()

processor = get_processor()

# Barra lateral com navegação
st.sidebar.markdkow("## 🎯 Menu de Navegawão")
app_mode = st.sidebar.radio(
    "Escoha um modo:",
    ["🏠 Inicial", "🎀️ Processamento de Imagem", "🎸 ��� Webcam em Tempo Real", 
🎁 Detecação de Faces", "📚 Aálise de Qualidade", "📸 Exportar Resultados"]
)

# Modo: Página Inicial
if app_mode == "🏠 Inicial":
    st.markdown('<div class="section-header">Bem-vindo  à Visão Computacional Pro</div>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown(`&### Funcionalidades
        
☫ 🞠 "Inuíal"☬
        - Filtras avançados (Blur, Sharpen, Canny)�  
   `