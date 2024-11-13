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

# def get_connection():
#     conn = psycopg2.connect(
#         host="localhost",
#         database="bd_rosat",
#         user="usuario_rosat",     # Cambia esto según el usuario de tu base de datos
#         password="lauraana"  # Cambia esto por la contraseña de tu base de datos
#     )
#     return conn

# Función para ejecutar consultas
def run_query(query, params=()):
    conn = get_connection()
    try:
        with conn.cursor() as cursor:
            cursor.execute(query, params)
            return cursor.fetchall()
    finally:
        conn.close()
