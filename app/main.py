from flask import Flask
from flask import request, render_template, redirect
from conexion import BaseDeDatos

import forms
# se instancia la base de datos para poder usarla en el proyecto
db = BaseDeDatos()

app = Flask(__name__)
app.secret_key = 'superclave'

@app.route('/', methods=['GET', 'POST'])
def tareas():
    lista_dics_tareas = db.leer_tareas()
    return render_template('tasks.html', lista_dics_tareas=lista_dics_tareas)


@app.route('/agregar/', methods=['GET', 'POST'])
def agregar_tarea():
    tareas_form = forms.Tarea(request.form)
    if request.method == 'POST':
        db.insertar_tarea(tareas_form.descripcion.data)
        return redirect('/')
    return render_template('agregar_tarea.html', tareas_form=tareas_form)


if __name__ == '__main__':
    app.run(debug=True)
