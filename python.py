import streamlit as st
import os
import json

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
    # Incluir el código para generar la encuesta aquí (el código de generar encuesta ya compartido)
    # Puedes copiar el bloque de código de creación de encuesta de la versión anterior.
    # Por ejemplo:
    title = st.text_input("Título de la encuesta", "Mi Encuesta")
    description = st.text_area("Descripción o tema de la encuesta", "Escribe una descripción o tema.")
    # Resto del código...
    
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
