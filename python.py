import streamlit as st
import pandas as pd
import random
import string

# Función para generar un enlace único
def generar_enlace():
    base_url = "https://valeryhugohalloween2024.streamlit.app//Survey"  # Enlace actualizado para la página Survey
    return base_url

# Variables de estado para opciones dinámicas
if 'opciones' not in st.session_state:
    st.session_state.opciones = []
if 'enlace_id' not in st.session_state:
    st.session_state.enlace_id = ''.join(random.choices(string.ascii_lowercase + string.digits, k=6))

# Establecer color de fondo de la página principal a negro
st.markdown(
    """
    <style>
    .stApp {
        background-color: black;
        color: white;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Título principal
st.title("Generador de Encuestas")

# Sección para personalizar la encuesta
st.header("Crea tu encuesta")
title = st.text_input("Título de la encuesta", "Mi Encuesta")
description = st.text_area("Descripción o tema de la encuesta", "Escribe una descripción o tema.")
bg_color = st.color_picker("Elige el color de fondo de la encuesta", "#ffffff")

# Botón para agregar opciones dinámicamente
if st.button("Agregar opción"):
    st.session_state.opciones.append(f"Opción {len(st.session_state.opciones) + 1}")

# Mostrar las opciones en una tabla
if st.session_state.opciones:
    df_opciones = pd.DataFrame(st.session_state.opciones, columns=["Opciones"])
    st.table(df_opciones)

# Eliminar última opción
if st.button("Eliminar última opción"):
    if st.session_state.opciones:
        st.session_state.opciones.pop()

# Generar enlace de la encuesta
if st.button("Generar encuesta"):
    if st.session_state.opciones:
        st.success(f"Encuesta '{title}' creada exitosamente.")
        
        # Guardar en el estado los datos para la encuesta
        st.session_state.titulo_encuesta = title
        st.session_state.descripcion_encuesta = description
        st.session_state.color_fondo_encuesta = bg_color
        
        enlace_encuesta = generar_enlace()
        st.write(f"Encuesta disponible en: [Haz clic aquí para contestar]({enlace_encuesta})")
    else:
        st.error("Debes agregar al menos una opción para generar la encuesta.")
