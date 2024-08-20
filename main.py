import os
import sys
import streamlit as st
import yaml
from app.adapters.streamlit_adapter import StreamlitAdapter
from app.adapters.file_adapter import FileAdapter
from app.adapters.claude_adapter import ClaudeAdapter, set_api_key
from app.domain.services import ConfigurationService

# Configuración de la página
st.set_page_config(
    page_title="Generador de Configuración - Plataforma A",
    page_icon="🛠️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Estilos CSS personalizados
st.markdown("""
    <style>
    .main .block-container {padding-top: 1rem;}
    .stAlert {background-color: #f0f2f6; border: none; color: #31333F;}
    .stButton>button {width: 100%;}
    .stTextArea>div>div>textarea {font-family: monospace;}
    </style>
    """, unsafe_allow_html=True)

# Carga de configuración
@st.cache_resource
def load_config():
    with open('config/config.yaml', 'r') as config_file:
        return yaml.safe_load(config_file)

config = load_config()

# Configurar la API key globalmente
set_api_key(config['claude_api_key'])

# Inicialización de servicios
file_adapter = FileAdapter()
claude_adapter = ClaudeAdapter()  # Ya no necesitas pasar la API key aquí
ui_adapter = StreamlitAdapter()
config_service = ConfigurationService(file_adapter, claude_adapter)

def main():
    st.title("🛠️ Generador de Configuración para Plataforma A")
    st.markdown("---")

    # Sidebar
    with st.sidebar:
        st.header("📁 Cargar Archivos")
        uploaded_files = st.file_uploader("Seleccionar archivos", accept_multiple_files=True, type=['txt'])
        
        st.header("⚙️ Configuración de Hiperparámetros")
        temperature = st.slider("Temperature", 0.0, 1.0, 0.7, help="Controla la aleatoriedad de la salida")
        max_tokens = st.number_input("Max Tokens", 100, 2000, 1000, help="Número máximo de tokens en la respuesta")

    # Contenido principal
    if uploaded_files:
        file_contents = {file.name: file.getvalue().decode() for file in uploaded_files}

        # Generar y mostrar prompt
        prompt = config_service.generate_prompt(file_contents)
        with st.expander("🔍 Ver Prompt Generado", expanded=False):
            st.text_area("Prompt Generado", prompt, height=300, disabled=True)

        # Columnas para entrada y salida
        col1, col2 = st.columns(2)

        with col1:
            st.header("📄 Contenido de entrada.txt")
            if 'entrada.txt' in file_contents:
                st.text_area("Contenido de entrada", file_contents['entrada.txt'], height=400, key="input_content")
            else:
                st.error("❌ Archivo entrada.txt no encontrado")

        with col2:
            st.header("🤖 Archivo propuesto")
            if st.button("🚀 Generar Configuración"):
                with st.spinner("Generando configuración..."):
                    try:
                        response = config_service.generate_configuration(prompt, temperature, max_tokens)
                        st.text_area("Respuesta generada", response, height=400, key="output_content")
                        st.success("✅ Configuración generada exitosamente")
                    except Exception as e:
                        st.error(f"❌ Error al generar la configuración: {str(e)}")
    else:
        st.info("👆 Por favor, carga los archivos necesarios en la barra lateral para comenzar.")

    # Pie de página
    st.markdown("---")
    st.markdown("Desarrollado con ❤️ por Mauricio Daza Becerra | Cod. 2240584")

if __name__ == "__main__":
    main()