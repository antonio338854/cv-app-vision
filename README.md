# 👁️ Visão Computacional Pro

Uma aplicação completa de processamento de imagens e visão computacional, construída com Python, OpenCV e Streamlit.

## ✨ Funcionalidades

- **Processamento de Imagem**: Filtros avançados (Blur, Sharpen, Canny Edge)
- **Conversão de Cores**: RGB, HSV, Grayscale, Sepia
- **Detecção de Faces**: Reconhecimento e contagem em tempo real
- **Análise de Qualidade**: Métricas de nitidez, contraste e brilho
- **Exportação**: Download de imagens processadas

## 🚀 Instalação

```bash
git clone https://github.com/antonio338854/cv-app-vision.git
cd cv-app-vision
pip install -r requirements.txt
streamlit run app.py
```

## 💻 Uso

A aplicação abrirá em `http://localhost:8501`

### Exemplos

1. **Processamento de Imagem**: Faça upload → Selecione filtro → Baixe resultado
2. **Detecção de Faces**: Carregue imagem → Detecção automática
3. **Análise de Qualidade**: Verifique métricas de qualidade

## 🏗️ Estrutura

```
cv-app-vision/
├── app.py                  # Aplicação principal
├── vision_processor.py     # Processador de visão
├── requirements.txt        # Dependências
└── README.md              # Este arquivo
```

## 🔧 Funcionalidades Detalhadas

### Processamento de Imagem
- Blur (Desfoque)
- Sharpen (Nitidez)
- Canny Edge Detection
- Conversão para Grayscale
- Conversão para HSV
- Efeito Sepia

### Análise de Qualidade
- Medição de nitidez (Laplacian Variance)
- Análise de contraste
- Medição de brilho
- Estatísticas gerais da imagem

### Detecção de Faces
- Detecção em tempo real
- Contagem de faces
- Marcação visual

## 📝 Licença

MIT License
