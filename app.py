# app.py
import streamlit as st
from pages import avisos, articulos, clientes, aparatos, marcas, empleados, grupos, login
from utils.auth import check_auth

def mostrar_pagina(pagina):
    if pagina == "Avisos":
        avisos.mostrar()
    elif pagina == "Articulos":
        articulos.mostrar()
    elif pagina == "Clientes":
        clientes.mostrar()
    elif pagina == "Aparatos":
        aparatos.mostrar()
    elif pagina == "Marcas":
        marcas.mostrar()
    elif pagina == "Empleados":
        empleados.mostrar()
    elif pagina == "Grupos":
        grupos.mostrar()
    elif pagina == "Login":
        login.mostrar()

# Configuración de la interfaz de Streamlit
st.set_page_config(page_title="Mi Aplicación CRUD", layout="wide")
st.sidebar.title("Dashboard")

# Autenticación
if check_auth():
    # Opciones del menú
    pagina = st.sidebar.selectbox("Seleccione una opción", [
        "Avisos", "Articulos", "Clientes", "Aparatos", "Marcas", "Empleados", "Grupos", "Salir"
    ])

    if pagina == "Salir":
        st.sidebar.write("Has cerrado sesión.")
    else:
        mostrar_pagina(pagina)
else:
    login.mostrar()
