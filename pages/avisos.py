# pages/avisos.py
import streamlit as st
from utils.db import obtener_avisos, agregar_aviso, actualizar_aviso, eliminar_aviso

def mostrar():
    st.title("Módulo de Avisos")
    
    # Mostrar avisos existentes
    avisos = obtener_avisos()
    st.table(avisos)

    # Formulario para agregar un nuevo aviso
    with st.form("Agregar Aviso"):
        titulo = st.text_input("Título del Aviso")
        contenido = st.text_area("Contenido del Aviso")
        submit = st.form_submit_button("Agregar")
        if submit:
            agregar_aviso(titulo, contenido)
            st.success("Aviso agregado correctamente")

    # Formulario para actualizar o eliminar avisos
    aviso_id = st.selectbox("Selecciona un aviso para editar", [a['id'] for a in avisos])
    nuevo_titulo = st.text_input("Nuevo Título")
    nuevo_contenido = st.text_area("Nuevo Contenido")
    if st.button("Actualizar Aviso"):
        actualizar_aviso(aviso_id, nuevo_titulo, nuevo_contenido)
        st.success("Aviso actualizado")
    if st.button("Eliminar Aviso"):
        eliminar_aviso(aviso_id)
        st.warning("Aviso eliminado")
