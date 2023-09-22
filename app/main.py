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


@app.route('/modificar/', methods=['GET', 'POST'])
def modificar_tarea():
    lista_dics_tareas = db.leer_tareas()
    tareas_form = forms.Tarea(request.form)
    if request.method == 'POST':
        id_tarea = tareas_form.id.data
        if id_tarea:
            eliminar_tarea = tareas_form.eliminar.data
            tarea_hecha, tarea_no_hecha = tareas_form.hecha.data, tareas_form.no_hecha.data
            if eliminar_tarea:
                db.eliminar_tarea(id_tarea)
            elif tarea_hecha:
                db.cambiar_estado_tarea(id_tarea, True)
            elif tarea_no_hecha:
                db.cambiar_estado_tarea(id_tarea, False)
    return render_template('modificar_tarea.html', tareas_form=tareas_form, lista_dics_tareas=lista_dics_tareas)


if __name__ == '__main__':
    app.run(debug=True)
