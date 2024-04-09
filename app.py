from flask import Flask, request
from flask_restx import Resource, Api
from flask_cors import CORS

from model.generator import generate


app = Flask(__name__)
CORS(app)
api = Api(app)
    
@api.route('/text/<string:text>')
class TodoSimple(Resource):
    def get(self, text):
        return {
            'genetrated': generate(text),
        }

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)