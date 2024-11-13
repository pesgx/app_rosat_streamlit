import streamlit as st
from utils.db import run_query, add_data

def gestionar_avisos():
    st.title("Gestión de Avisos")

    # Mostrar avisos existentes
    resultados = run_query("SELECT * FROM avisos")
    st.write("Avisos existentes:")
    for row in resultados:
        st.write(row)

    # Crear nuevo aviso
    st.subheader("Crear Aviso")
    numero_aviso = st.text_input("Número de Aviso")
    cliente_id = st.number_input("ID Cliente", min_value=1)
    aparato_id = st.number_input("ID Aparato", min_value=1)
    empleado_id = st.number_input("ID Empleado", min_value=1)
    observaciones = st.text_area("Observaciones")

    if st.button("Añadir Aviso"):
        aviso_id = add_data("INSERT INTO avisos (numero_aviso, cliente_id, aparato_id, empleado_id, observaciones) VALUES (?, ?, ?, ?, ?)",
                            (numero_aviso, cliente_id, aparato_id, empleado_id, observaciones))
        st.success("Aviso añadido")

    # Gestión de líneas de aviso
    st.subheader("Líneas de Aviso")
    aviso_seleccionado = st.selectbox("Selecciona un Aviso", [r[0] for r in resultados])

    lineas_resultados = run_query("SELECT * FROM lineas_aviso WHERE aviso_id = ?", (aviso_seleccionado,))
    st.write("Líneas del aviso:")
    for linea in lineas_resultados:
        st.write(linea)

    # Añadir línea de aviso
    articulo_id = st.number_input("ID Artículo", min_value=1)
    cantidad = st.number_input("Cantidad", min_value=1)
    precio_unitario = st.number_input("Precio Unitario")

    if st.button("Añadir Línea"):
        add_data("INSERT INTO lineas_aviso (aviso_id, articulo_id, cantidad, precio_unitario) VALUES (?, ?, ?, ?)",
                (aviso_seleccionado, articulo_id, cantidad, precio_unitario))
        st.success("Línea añadida")

    # Opciones para eliminar y actualizar
    linea_id = st.selectbox("ID Línea para modificar", [l[0] for l in lineas_resultados])

    if st.button("Eliminar Línea"):
        run_query("DELETE FROM lineas_aviso WHERE id = ?", (linea_id,))
        st.success("Línea eliminada")
