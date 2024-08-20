import streamlit as st
from app.ports.ui_port import UIPort

class StreamlitAdapter(UIPort):
    def display_text(self, text, header=None):
        if header:
            st.subheader(header)
        st.text(text)

    def get_user_input(self, input_type, label, **kwargs):
        if input_type == 'text':
            return st.text_input(label, **kwargs)
        elif input_type == 'file':
            return st.file_uploader(label, **kwargs)
        elif input_type == 'button':
            return st.button(label, **kwargs)
        # Agregar más tipos de entrada según sea necesario
