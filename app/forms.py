from wtforms import StringField, SubmitField
from flask_wtf import FlaskForm

class Tarea(FlaskForm):
    descripcion = StringField('Descripcion de la tarea')
    submit = SubmitField('Enviar')