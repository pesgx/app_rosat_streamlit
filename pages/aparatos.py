import streamlit as st
from utils.db import run_query

def mostrar_aparatos():
    """
    Función para mostrar todos los registros de la tabla 'tabla_aparatos' en un DataFrame.
    """
    query = "SELECT * FROM tabla_aparatos ORDER BY id_aparato"
    aparatos = run_query(query)
    
    if aparatos:
        df = [{"ID": a[0], "Nombre": a[1]} for a in aparatos]
        return df
    return []

def gestionar_aparatos():
    """
    Función principal para la gestión del módulo CRUD de 'aparatos'
    """
    st.title("Gestión de Aparatos")

    # Campos de entrada activados
    id_aparato = st.number_input("ID del Aparato", min_value=1, step=1, key="id_aparato")
    nombre_aparato = st.text_input("Nombre del Aparato", key="nombre_aparato")

    # Botones para las acciones CRUD
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        agregar = st.button("AGREGAR")
    with col2:
        actualizar = st.button("ACTUALIZAR")
    with col3:
        eliminar = st.button("ELIMINAR")
    with col4:
        mostrar = st.button("MOSTRAR")

    # Lógica de operaciones CRUD
    if agregar:
        if nombre_aparato:
            query = "INSERT INTO tabla_aparatos (nombre_aparato) VALUES (%s)"
            run_query(query, (nombre_aparato,))
            st.success("Aparato agregado correctamente.")
        else:
            st.error("El nombre del aparato no puede estar vacío.")

    if actualizar:
        if id_aparato and nombre_aparato:
            query = "UPDATE tabla_aparatos SET nombre_aparato = %s WHERE id_aparato = %s"
            run_query(query, (nombre_aparato, id_aparato))
            st.success("Aparato actualizado correctamente.")
        else:
            st.error("Debes seleccionar un aparato y proporcionar un nombre nuevo.")

    if eliminar:
        if id_aparato:
            query = "DELETE FROM tabla_aparatos WHERE id_aparato = %s"
            run_query(query, (id_aparato,))
            st.success("Aparato eliminado correctamente.")
        else:
            st.error("Debes seleccionar un aparato para eliminar.")

    # Tabla de visualización de datos
    st.write("### Lista de Aparatos")
    datos_aparatos = mostrar_aparatos()
    if datos_aparatos:
        df_aparatos = st.dataframe(datos_aparatos)

        # Selección de un aparato en la tabla para autocompletar campos
        selected_id = st.selectbox("Selecciona el ID del aparato para autocompletar", [dato["ID"] for dato in datos_aparatos])
        if mostrar:
            # Autocompleta los campos 'id_aparato' y 'nombre_aparato' con los datos seleccionados
            aparato = next((a for a in datos_aparatos if a["ID"] == selected_id), None)
            if aparato:
                st.session_state["id_aparato"] = aparato["ID"]
                st.session_state["nombre_aparato"] = aparato["Nombre"]

