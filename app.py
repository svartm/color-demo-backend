from flask import Flask, request, jsonify
from flask_cors import CORS
from color_helper import process_guess, generate_hex_color
import random

app = Flask(__name__)
CORS(app)  # Enable CORS for all origins

@app.route('/getcolor', methods=['GET'])
def get_new_color():
    color_code = generate_hex_color()
    return jsonify({"color": color_code})

@app.route('/checkcolor', methods=['POST'])
def check_color():
    data = request.get_json()
    answer = data['answer']
    guess = data['guess']
    message = process_guess(answer, guess)
    return jsonify({"message": message})

if __name__ == '__main__':
    app.run(debug=True)
