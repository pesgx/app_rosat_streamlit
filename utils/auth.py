import streamlit as st
from utils.db import run_query

# Función de autenticación
def authenticate(nombre_usuario, contrasena):
    # Consulta a la tabla de usuarios
    query = "SELECT contrasena FROM tabla_usuarios WHERE nombre_usuario = %s"
    resultado = run_query(query, (nombre_usuario,))

    # Verificación de la contraseña
    if resultado:
        contrasena_db = resultado[0][0]  # Obtenemos la contraseña de la base de datos
        return contrasena == contrasena_db  # Verifica si coincide
    return False

# Función para el manejo de inicio de sesión
def login():
    st.sidebar.title("Iniciar Sesión")
    nombre_usuario = st.sidebar.text_input("Usuario")
    contrasena = st.sidebar.text_input("Contraseña", type="password")

    if st.sidebar.button("Ingresar"):
        if authenticate(nombre_usuario, contrasena):
            st.success("Inicio de sesión exitoso")
            st.session_state["authenticated"] = True
        else:
            st.error("Usuario o contraseña incorrectos")
