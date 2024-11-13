# utils/auth.py
import streamlit as st

def check_auth():
    # Autenticación simple
    usuario = st.sidebar.text_input("Usuario")
    contrasena = st.sidebar.text_input("Contraseña", type="password")
    if usuario == "a" and contrasena == "a":
        st.session_state["autenticado"] = True
    return st.session_state.get("autenticado", False)
