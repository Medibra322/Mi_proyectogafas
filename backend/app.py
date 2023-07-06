from flask import Flask
from routes.gafas import *


app = Flask(__name__)


@app.route("/", methods=["GET"])
def hello():
    return "Hello World!"


app.route('/gafas', methods=['GET'])(get_gafas)


if __name__ == '__main__':
    app.run(debug=True)
