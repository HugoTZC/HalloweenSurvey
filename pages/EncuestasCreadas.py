import streamlit as st
import os
import json

# Función para cargar encuesta desde archivo JSON
def cargar_encuesta(enlace_id):
    file_name = f"{enlace_id}.json"
    if os.path.exists(file_name):
        with open(file_name, "r") as f:
            return json.load(f)
    return None

st.title("Encuestas creadas")

# Mostrar las encuestas guardadas
encuestas = [f.split(".")[0] for f in os.listdir() if f.endswith(".json")]
if encuestas:
    encuesta_seleccionada = st.selectbox("Selecciona una encuesta para ver los resultados:", encuestas)
    if encuesta_seleccionada:
        st.write(f"Resultados de la encuesta: {encuesta_seleccionada}")
        # Cargar la encuesta y mostrar sus resultados
        encuesta_data = cargar_encuesta(encuesta_seleccionada)
        if encuesta_data:
            total_votos = sum(encuesta_data.get("votos", {}).values())
            for opcion, votos in encuesta_data.get("votos", {}).items():
                porcentaje = (votos / total_votos * 100) if total_votos > 0 else 0
                st.write(f"{opcion}: {porcentaje:.2f}% ({votos} votos)")
else:
    st.write("No se han creado encuestas.")
