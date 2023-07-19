from flask import jsonify, make_response
from database.db import connectdb


def get_gafas():
    conn = connectdb()
    cur = conn.cursor()
    try:
        cur.execute('SELECT * FROM gafas')
        datos_gafas = cur.fetchall()
        data = [{'id_gafas': dato[1],'nombre': dato[2], 'correo': dato[3], 'celular': dato[4], 'mensaje': dato[5]} for dato in datos_gafas]
        conn.close()

        response = make_response(jsonify(data))
        response.status_code = 200  # Código de estado 200 (OK)
    except:
        # Manejo de errores en caso de fallo en la consulta o conexión a la base de datos
        conn.close()
        response = make_response("Error en la consulta a la base de datos", 500)  # Código de estado 500 (Internal Server Error)

    return response

def obtener_gafas_por_id(id_gafas):
    conn = connectdb()
    cur = conn.cursor()
    cur.execute('SELECT * FROM gafas WHERE id_gafas = %s', (id_gafas,))
    dato_gafas = cur.fetchone()

    if dato_gafas:
        dato = {'id_gafas': dato_gafas[1],'nombre': dato_gafas[2], 'correo': dato_gafas[3], 'celular': dato_gafas[4], 'mensaje': dato_gafas[5]}
        conn.close()
        return jsonify(dato)
    else:
        return 'gafas no encontrado'