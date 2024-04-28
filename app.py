from flask import Flask, request
from flask_restx import Resource, Api
from flask_cors import CORS

from utils import model
from utils import order_processing

app = Flask(__name__)
CORS(app)
api = Api(app)
    
@api.route('/text/<string:text>')
class TodoSimple(Resource):
    def get(self, text):
        generated_text = model.generate(text)
        processed_text = order_processing.text_to_json(generated_text)
        return processed_text

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)