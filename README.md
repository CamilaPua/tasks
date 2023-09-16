# Como usar app de flask
Corra estos comandos en su terminal
```bash
python3 -m venv env
```
Activa el entorno virtual, este comando puede variar segun tu sistema operativo
```bash
env\Scripts\activate
```
```bash
pip install -r requirements.txt
```
Este comando activa la app en el 127.0.0.1:5000
```bash
python app/main.py
```

## Observaciones
- Se ha cargado la base de datos, usa el motor de Access

- En el archivo app/conexion.py se usan variables de entorno, ignore de la linea 1 a la 5 y reemplaze en la linea 11 RUTA_DB por su ruta a la base de datos