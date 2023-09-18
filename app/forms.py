from wtforms import StringField, SubmitField, IntegerField
from flask_wtf import FlaskForm

class Tarea(FlaskForm):
    id = IntegerField('ID de la tarea')
    descripcion = StringField('Descripcion de la tarea')
    hecha = SubmitField('Hecha')
    submit = SubmitField('Enviar')