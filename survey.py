import streamlit as st

# Leer los parámetros de la URL
query_params = st.experimental_get_query_params()
encuesta_id = query_params.get('encuesta', [''])[0]

# Verificar si los datos de la encuesta están almacenados en el estado
if encuesta_id and 'opciones' in st.session_state and st.session_state.enlace_id == encuesta_id:
    # Aplicar el color de fondo de la encuesta
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-color: {st.session_state.color_fondo_encuesta};
        }}
        </style>
        """,
        unsafe_allow_html=True
    )
    
    # Mostrar la encuesta
    st.title(st.session_state.titulo_encuesta)
    st.write(st.session_state.descripcion_encuesta)
    
    # Mostrar las opciones de la encuesta
    seleccion = st.radio("Elige una opción:", st.session_state.opciones)
    
    # Botón para enviar la respuesta
    if st.button("Enviar respuesta"):
        st.success("Respuesta enviada con éxito.")
else:
    st.error("No se encontró la encuesta o los datos han expirado.")
