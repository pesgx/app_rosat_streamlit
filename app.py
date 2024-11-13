import streamlit as st
from utils.auth import login
from pages import avisos, articulos, clientes, aparatos, marcas, empleados, grupos

# Autenticación
if "authenticated" not in st.session_state:
    st.session_state["authenticated"] = False

if not st.session_state["authenticated"]:
    login()
else:
    # Menú lateral
    st.sidebar.title("Menú de Navegación")
    menu = st.sidebar.radio("Selecciona un módulo:", 
                            ("Avisos", "Artículos", "Clientes", "Aparatos", "Marcas", "Empleados", "Grupos"))

    if menu == "Avisos":
        avisos.gestionar_avisos()
    elif menu == "Artículos":
        articulos.gestionar_articulos()
    elif menu == "Clientes":
        clientes.gestionar_clientes()
    elif menu == "Aparatos":
        aparatos.gestionar_aparatos()
    elif menu == "Marcas":
        marcas.gestionar_marcas()
    elif menu == "Empleados":
        empleados.gestionar_empleados()
    elif menu == "Grupos":
        grupos.gestionar_grupos()
