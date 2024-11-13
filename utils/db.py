import sqlite3
import os

# Ruta de la base de datos
DB_PATH = os.path.join("data", "database.sqlite3")

# Conexión a la base de datos
def get_connection():
    return sqlite3.connect(DB_PATH)

# Función para ejecutar una consulta
def run_query(query, params=()):
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(query, params)
        conn.commit()
        return cursor.fetchall()

# Función para añadir datos
def add_data(query, params=()):
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(query, params)
        conn.commit()
        return cursor.lastrowid
