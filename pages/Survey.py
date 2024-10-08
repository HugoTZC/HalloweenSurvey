import streamlit as st
import json
import os

# Leer los parámetros de la URL
query_params = st.experimental_get_query_params()
encuesta_id = query_params.get('encuesta', [''])[0]

# Función para cargar encuesta desde archivo JSON
def cargar_encuesta(enlace_id):
    file_name = f"{enlace_id}.json"
    if os.path.exists(file_name):
        with open(file_name, "r") as f:
            return json.load(f)
    return None

# Función para guardar votos
def guardar_votos(enlace_id, encuesta_data):
    with open(f"{enlace_id}.json", "w") as f:
        json.dump(encuesta_data, f)

# Verificar si el archivo de la encuesta existe y cargar los datos
encuesta_data = cargar_encuesta(encuesta_id)

if encuesta_data:
    # Aplicar el color de fondo de la encuesta
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-color: {encuesta_data['color_fondo']};
        }}
        </style>
        """,
        unsafe_allow_html=True
    )
    
    # Mostrar la encuesta
    st.title(encuesta_data['titulo'])
    st.write(encuesta_data['descripcion'])
    
    # Mostrar las opciones de la encuesta
    seleccion = st.radio("Elige una opción:", encuesta_data['opciones'])
    
    # Botón para enviar la respuesta
    if st.button("Enviar respuesta"):
        if 'votos' not in encuesta_data:
            encuesta_data['votos'] = {opcion: 0 for opcion in encuesta_data['opciones']}
        
        encuesta_data['votos'][seleccion] += 1
        guardar_votos(encuesta_id, encuesta_data)
        st.success("Respuesta enviada con éxito.")
else:
    st.error("No se encontró la encuesta o los datos han expirado.")
