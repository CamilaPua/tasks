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

    def completar_tarea(self, id_tarea):
        query = " UPDATE tareas SET Estado = Si WHERE Id = ?;"
        self.cursor.execute(query, id_tarea)
        self.conexion.commit()
    
    def eliminar_tarea(self, id_tarea):
        query = "DELETE FROM Empleados WHERE ID = ?"
        self.cursor.execute(query, id_tarea)
        self.conexion.commit()

    def leer_tareas(self):
        self.cursor.execute("SELECT * FROM tareas")
        return self.cursor.fetchall()


if __name__ == '__main__':
    # se instancia la base de datos para poder usarla en el proyecto
    db = BaseDeDatos()

    # se llena la base de datos
    # tareas = [
    #     'Llenar la jarra',
    #     'Hacer deploy',
    #     'Organizar el cuarto',
    #     'barrer el cuarto',
    #     'Estudiar algoritmos 2',
    #     'Lavar ropa',
    #     'Revisar material de SED'
    # ]
    # for tarea in tareas:
    #     db.insertar_tarea(tarea)
    db.leer_tareas()
