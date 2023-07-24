
from routes.gafas import *
from flask import Flask, request, jsonify
from flask_cors import CORS


app = Flask(__name__)
cors = CORS(app)


@app.route("/", methods=["GET"])
def hello():
    return "Hello World!"


app.route('/gafas', methods=['GET'])(get_gafas)
app.route('/gafas/<int:id_gafas>')(obtener_gafas_por_id)
app.route('/gafas', methods=['POST'])(add_gafas)
app.route('/gafas/<int:id_gafas>', methods=['DELETE'])(del_gafas)
app.route("/gafas/<int:id_gafas>", methods=["PATCH"])(update_gafas)


if __name__ == '__main__':
    app.run(debug=True)
