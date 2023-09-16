from flask import Flask, request, render_template
from conexion import BaseDeDatos

# se instancia la base de datos para poder usarla en el proyecto
db = BaseDeDatos()

app = Flask(__name__)

@app.route('/')
def tareas():
    tareas = db.leer_tareas()
    return render_template('tasks.html', tareas=tareas)

if __name__ == '__main__':
    app.run(debug=True)
