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

# Función para guardar los cambios en la encuesta
def guardar_encuesta(enlace_id, encuesta_data):
    with open(f"{enlace_id}.json", "w") as f:
        json.dump(encuesta_data, f)

# Comprobar si el usuario ya ha votado
if 'voto_realizado' not in st.session_state:
    st.session_state.voto_realizado = False

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
    
    # Si la encuesta está cerrada, mostrar mensaje
    if encuesta_data.get("cerrada", False):
        st.error("Esta encuesta ya está cerrada. No se puede votar.")
    elif st.session_state.voto_realizado:
        # Redirigir a la página de "Gracias" si ya votó
        st.experimental_set_query_params(page="thanks")
        st.stop()
    else:
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
            guardar_encuesta(encuesta_id, encuesta_data)
            
            # Marcar como votado
            st.session_state.voto_realizado = True
            
            # Redirigir a la página de "Gracias"
            st.experimental_set_query_params(page="thanks")
            st.stop()
else:
    st.error("No se encontró la encuesta o los datos han expirado.")
