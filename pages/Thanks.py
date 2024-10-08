import streamlit as st

st.title("¡Gracias por tu respuesta!")
st.write("Ya has votado en esta encuesta. No es posible volver a votar desde este dispositivo.")

# Botón de regreso a la página principal o a otra sección
if st.button("Regresar al inicio"):
    st.experimental_rerun("https://valeryhugohalloween2024.streamlit.app/")
