import psycopg2
import os
import streamlit as st

# Configuración de la conexión a la base de datos
def get_connection():
    conn = psycopg2.connect(
        host="localhost",
        database="bd_rosat",
        user="postgres",     # Cambia esto según el usuario de tu base de datos
        password="pescacom_2"  # Cambia esto por la contraseña de tu base de datos
    )
    return conn

# Función para ejecutar consultas
def run_query(query, params=()):
    conn = get_connection()
    try:
        with conn.cursor() as cursor:
            cursor.execute(query, params)
            # Solo realizar fetchall() si es una consulta SELECT
            if query.strip().lower().startswith("select"):
                return cursor.fetchall()
            conn.commit()  # Confirma la transacción para INSERT, UPDATE y DELETE
    finally:
        conn.close()
