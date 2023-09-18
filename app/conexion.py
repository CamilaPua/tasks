# trae variables de entorno
import os
from dotenv import load_dotenv
load_dotenv()
RUTA_DB = os.environ.get("RUTA_DB")

from pyodbc import connect

class BaseDeDatos:
    def __init__(self) -> None:
        self.conexion = connect(r"Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ="+RUTA_DB+";")
        self.cursor = self.conexion.cursor()

    def insertar_tarea(self, tarea):
        query = "INSERT INTO tareas (Descripcion, Estado) \
        VALUES (?, No)"
        self.cursor.execute(query, (tarea))
        self.conexion.commit()

    def cambiar_estado_tarea(self, id, estado):
        query = " UPDATE tareas SET Estado = ? WHERE Id = ?;"
        self.cursor.execute(query, estado, id)
        self.conexion.commit()
    
    def eliminar_tarea(self, id_tarea):
        query = "DELETE FROM tareas WHERE ID = ?"
        self.cursor.execute(query, id_tarea)
        self.conexion.commit()

    def leer_tareas(self):
        self.cursor.execute("SELECT * FROM tareas")
        tareas = self.cursor.fetchall()
        lista_dicts_tareas = []
        for tarea in tareas:
            id, descripcion, estado = tarea
            atributos = ['id', 'descripcion', 'estado']
            valores = [id, descripcion, estado]
            dict_tarea = dict(zip(atributos, valores))
            lista_dicts_tareas.append(dict_tarea)
        return lista_dicts_tareas


if __name__ == '__main__':
    # se instancia la base de datos para poder usarla en el proyecto
    db = BaseDeDatos()
    db.leer_tareas()
