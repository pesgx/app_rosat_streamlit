# utils/db.py
import sqlite3

def conectar_bd():
    return sqlite3.connect("data/database.sqlite3")

def obtener_avisos():
    conn = conectar_bd()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM avisos")
    avisos = cursor.fetchall()
    conn.close()
    return avisos

def agregar_aviso(titulo, contenido):
    conn = conectar_bd()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO avisos (titulo, contenido) VALUES (?, ?)", (titulo, contenido))
    conn.commit()
    conn.close()

def actualizar_aviso(id_aviso, titulo, contenido):
    conn = conectar_bd()
    cursor = conn.cursor()
    cursor.execute("UPDATE avisos SET titulo = ?, contenido = ? WHERE id = ?", (titulo, contenido, id_aviso))
    conn.commit()
    conn.close()

def eliminar_aviso(id_aviso):
    conn = conectar_bd()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM avisos WHERE id = ?", (id_aviso,))
    conn.commit()
    conn.close()
