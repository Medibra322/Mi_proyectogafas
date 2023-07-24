from flask import jsonify, make_response, request
# import mysql.connector
from database.db import connectdb




def get_gafas():
    conn = connectdb()
    cur = conn.cursor()
    try:
        cur.execute('SELECT * FROM gafas')
        datos_gafas = cur.fetchall()
        data = [{'id_gafas': dato[0],'nombre': dato[1], 'correo': dato[2], 'celular': dato[3], 'mensaje': dato[4]} for dato in datos_gafas]
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
        dato = {'id_gafas': dato_gafas[0],'nombre': dato_gafas[1], 'correo': dato_gafas[2], 'celular': dato_gafas[3], 'mensaje': dato_gafas[4]}
        conn.close()
        return jsonify(dato)
    else:
        return 'gafas no encontrado'
    
def add_gafas():
    try:
        conn = connectdb()
        cur = conn.cursor()
        data = request.get_json()
        
        nombre = data['nombre']
        correo = data['correo']
        celular = data['celular']
        mensaje = data['mensaje']

        cur.execute('INSERT INTO gafas (nombre, correo, celular, mensaje) VALUES (%s, %s, %s, %s)', (nombre, correo, celular, mensaje))
        conn.commit()
        print('gafas creado')
        return jsonify({"message": "Mensaje recibido correctamente"}),200
    except connectdb.Error as error:
        return jsonify({'Error': str(error)}),500
    finally:
        conn.close()

from flask import make_response, jsonify

def del_gafas(id_gafas):
    conn = connectdb()
    cur = conn.cursor()
    cur.execute('DELETE FROM gafas WHERE id_gafas = %s', (id_gafas,))
    conn.commit()
    conn.close()
    print("gafas eliminado !!")
    return "gafas eliminado !!"


def update_gafas(id_gafas):
    conn = connectdb()
    cur = conn.cursor()

    data = request.get_json()

    if "nombre" in data:
        nombre = data["nombre"]
        cur.execute('UPDATE gafas SET nombre = %s WHERE id_gafas = %s', (nombre, id_gafas))

    if "correo" in data:
        correo = data["correo"]
        cur.execute('UPDATE gafas SET correo = %s WHERE id_gafas = %s', (correo, id_gafas))

    if "celular" in data:
        celular = data["celular"]
        cur.execute('UPDATE gafas SET celular = %s WHERE id_gafas = %s', (celular, id_gafas))
        
    if "mensaje" in data:
        mensaje = data["mensaje"]
        cur.execute('UPDATE gafas SET mensaje = %s WHERE id_gafas = %s', (mensaje, id_gafas))

    conn.commit()
    conn.close()

    return 'Dato modificado'