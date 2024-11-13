import streamlit as st
from utils.auth import login
from pages import (
    avisos, clientes, aparatos, marcas, empleados,
    grupos, compañias, usuarios, estados, poblaciones, agenda
)

# Imagen y título de bienvenida
st.image("assets/logo_ROSAT.png", width=150, use_container_width=True)

st.title("Gestión de avisos ROSAT")

# Autenticación
if "authenticated" not in st.session_state:
    st.session_state["authenticated"] = False

if not st.session_state["authenticated"]:
    login()
else:
    # Menú lateral
    st.sidebar.title("Menú de Navegación")
    menu = st.sidebar.radio(
        "Selecciona un módulo:",
        (
            "Avisos", "Clientes", "Aparatos", "Marcas", "Empleados",
            "Grupos", "Compañías", "Usuarios", "Estados", "Poblaciones", "Agenda"
        )
    )

    # Lógica para abrir cada módulo CRUD
    if menu == "Avisos":
        avisos.gestionar_avisos()
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
    elif menu == "Compañías":
        compañias.gestionar_compañias()
    elif menu == "Usuarios":
        usuarios.gestionar_usuarios()
    elif menu == "Estados":
        estados.gestionar_estados()
    elif menu == "Poblaciones":
        poblaciones.gestionar_poblaciones()
    elif menu == "Agenda":
        agenda.gestionar_agenda()
