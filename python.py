import streamlit as st
import os
import pandas as pd
import json
import random
import string

# Función para generar un enlace único
def generar_enlace(enlace_id):
    base_url = "https://valeryhugohalloween2024.streamlit.app/Survey"  # Enlace actualizado para la página Survey
    return f"{base_url}?encuesta={enlace_id}"

# Función para guardar encuesta en archivo JSON
def guardar_encuesta(enlace_id, titulo, descripcion, opciones, color_fondo):
    encuesta_data = {
        "titulo": titulo,
        "descripcion": descripcion,
        "opciones": opciones,
        "color_fondo": color_fondo,
        "votos": {opcion: 0 for opcion in opciones}  # Iniciar los votos en 0 para cada opción
    }
    with open(f"{enlace_id}.json", "w") as f:
        json.dump(encuesta_data, f)

# Función para navegar a la página de generación de encuestas
def navegar_a_generar():
    st.session_state['pagina_actual'] = 'generar'

# Función para navegar a la página de encuestas creadas
def navegar_a_encuestas_creadas():
    st.session_state['pagina_actual'] = 'encuestas_creadas'

# Inicializar la sesión
if 'pagina_actual' not in st.session_state:
    st.session_state['pagina_actual'] = 'generar'

# Barra lateral para navegar
st.sidebar.title("Opciones")
st.sidebar.button("Generar encuesta", on_click=navegar_a_generar)
st.sidebar.button("Encuestas creadas", on_click=navegar_a_encuestas_creadas)

# Navegar entre páginas
if st.session_state['pagina_actual'] == 'generar':
    st.title("Generar encuesta")

    # Sección para personalizar la encuesta
    title = st.text_input("Título de la encuesta", "Mi Encuesta")
    description = st.text_area("Descripción o tema de la encuesta", "Escribe una descripción o tema.")
    bg_color = st.color_picker("Elige el color de fondo de la encuesta", "#ffffff")

    # Inicializar las opciones de encuesta
    if 'opciones' not in st.session_state:
        st.session_state.opciones = []

    # Botón para agregar opciones dinámicamente
    if st.button("Agregar opción", key="add_option"):
        st.session_state.opciones.append(f"Opción {len(st.session_state.opciones) + 1}")

    # Mostrar las opciones en una tabla
    if st.session_state.opciones:
        df_opciones = pd.DataFrame(st.session_state.opciones, columns=["Opciones"])
        st.table(df_opciones)

    # Eliminar última opción
    if st.button("Eliminar última opción", key="delete_option"):
        if st.session_state.opciones:
            st.session_state.opciones.pop()

    # Generar enlace de la encuesta
    if st.button("Generar encuesta", key="generate_survey"):
        if st.session_state.opciones:
            enlace_id = ''.join(random.choices(string.ascii_lowercase + string.digits, k=6))
            guardar_encuesta(enlace_id, title, description, st.session_state.opciones, bg_color)
            enlace_encuesta = generar_enlace(enlace_id)
            st.success(f"Encuesta '{title}' creada exitosamente.")
            st.write(f"Encuesta disponible en: [Haz clic aquí para contestar]({enlace_encuesta})")
        else:
            st.error("Debes agregar al menos una opción para generar la encuesta.")

elif st.session_state['pagina_actual'] == 'encuestas_creadas':
    st.title("Encuestas creadas")
    st.write("Aquí aparecerán las encuestas creadas.")
    
    # Mostrar las encuestas guardadas
    encuestas = [f.split(".")[0] for f in os.listdir() if f.endswith(".json")]
    if encuestas:
        encuesta_seleccionada = st.selectbox("Selecciona una encuesta para ver los resultados:", encuestas)
        if encuesta_seleccionada:
            st.write(f"Resultados de la encuesta: {encuesta_seleccionada}")
            # Cargar la encuesta y mostrar sus resultados
            with open(f"{encuesta_seleccionada}.json", "r") as f:
                encuesta_data = json.load(f)
                total_votos = sum(encuesta_data.get("votos", {}).values())
                for opcion, votos in encuesta_data.get("votos", {}).items():
                    porcentaje = (votos / total_votos * 100) if total_votos > 0 else 0
                    st.write(f"{opcion}: {porcentaje:.2f}% ({votos} votos)")
    else:
        st.write("No se han creado encuestas.")
