import streamlit as st

# Simulación de una autenticación básica
USERS = {"a": "a"}

def authenticate(username, password):
    return USERS.get(username) == password

def login():
    st.sidebar.title("Iniciar Sesión")
    username = st.sidebar.text_input("Usuario")
    password = st.sidebar.text_input("Contraseña", type="password")
    if st.sidebar.button("Ingresar"):
        if authenticate(username, password):
            st.success("Inicio de sesión exitoso")
            st.session_state["authenticated"] = True
        else:
            st.error("Usuario o contraseña incorrectos")
