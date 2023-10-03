from flask import render_template

from . import RUTA, app
from .models import DBManager


@app.route('/')
def home():
    db = DBManager(RUTA)
    sql = 'SELECT id, fecha, concepto, tipo, cantidad FROM movimientos'
    movimientos = db.consultaSQL(sql)
    return render_template('inicio.html', movs=movimientos)


# - Función borrar  -- DONE
# - Operar con la BD
# - Botón de borrado en cada movimiento
# - Plantilla con el resultado -- DONE

@app.route('/borrar')
def eliminar():
    return render_template('borrado.html', resultado=False)
