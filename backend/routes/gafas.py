from flask import jsonify, make_response
from database.db import connectdb


def get_gafas():
    conn = connectdb()
    cur = conn.cursor()
    try:
        cur.execute('SELECT * FROM gafas')
        datos_gafas = cur.fetchall()
        data = [{'nombre': dato[1], 'correo': dato[2], 'celular': dato[3], 'mensaje': dato[4]} for dato in datos_gafas]
        conn.close()

        response = make_response(jsonify(data))
        response.status_code = 200  # Código de estado 200 (OK)
    except:
        # Manejo de errores en caso de fallo en la consulta o conexión a la base de datos
        conn.close()
        response = make_response("Error en la consulta a la base de datos", 500)  # Código de estado 500 (Internal Server Error)

    return response
