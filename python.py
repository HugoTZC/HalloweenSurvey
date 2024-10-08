import streamlit as st
import pandas as pd
import random
import string

# Función para generar un enlace único (hipervínculo)
def generar_enlace():
    base_url = "https://https://valeryhugohalloween2024.streamlit.app/"  # Reemplaza con la URL de tu app en Streamlit Cloud
    enlace_unico = ''.join(random.choices(string.ascii_lowercase + string.digits, k=6))
    return base_url + "?encuesta=" + enlace_unico

# Variables de estado para opciones dinámicas
if 'opciones' not in st.session_state:
    st.session_state.opciones = []

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
        enlace_encuesta = generar_enlace()
        st.write(f"Encuesta disponible en: [Haz clic aquí para contestar]({enlace_encuesta})")

        # Aplicar el color de fondo personalizado solo a la sección de la encuesta
        st.markdown(
            f"""
            <style>
            .stApp {{
                background-color: black;
                color: white;
            }}
            .reportview-container {{
                background-color: {bg_color};
            }}
            </style>
            """,
            unsafe_allow_html=True
        )
    else:
        st.error("Debes agregar al menos una opción para generar la encuesta.")
