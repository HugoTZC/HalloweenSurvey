import streamlit as st
import pandas as pd
import random
import string
import json

# Función para generar un enlace único
def generar_enlace(enlace_id):
    base_url = "https://valeryhugohalloween2024.streamlit.app/Survey"  # Tu enlace de la app
    return f"{base_url}?encuesta={enlace_id}"

# Función para guardar encuesta en archivo JSON
def guardar_encuesta(enlace_id, titulo, descripcion, opciones, color_fondo):
    encuesta_data = {
        "titulo": titulo,
        "descripcion": descripcion,
        "opciones": opciones,
        "color_fondo": color_fondo
    }
    with open(f"{enlace_id}.json", "w") as f:
        json.dump(encuesta_data, f)

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
        
        # Guardar los datos de la encuesta en un archivo JSON
        guardar_encuesta(st.session_state.enlace_id, title, description, st.session_state.opciones, bg_color)
        
        enlace_encuesta = generar_enlace(st.session_state.enlace_id)
        st.write(f"Encuesta disponible en: [Haz clic aquí para contestar]({enlace_encuesta})")
    else:
        st.error("Debes agregar al menos una opción para generar la encuesta.")
